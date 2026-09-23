import json
import subprocess
import os
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
MODEL = "claude-sonnet-4-20250514"
MAX_ITERATIONS = 15

# ─── Tools ───────────────────────────────────────────────────────

def read_file(path: str) -> str:
    try:
        return Path(path).read_text()
    except Exception as e:
        return f"Error: {e}"

def write_file(path: str, content: str) -> str:
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(content)
        return f"Wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"Error: {e}"

def run_command(cmd: str) -> str:
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=30
        )
        output = result.stdout + result.stderr
        return output[:5000]  # truncate long output
    except subprocess.TimeoutExpired:
        return "Error: command timed out"
    except Exception as e:
        return f"Error: {e}"

def search_codebase(pattern: str, directory: str = ".") -> str:
    try:
        result = subprocess.run(
            ["grep", "-rn", pattern, directory],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout[:3000] or "No matches found."
    except Exception as e:
        return f"Error: {e}"

TOOLS = {
    "read_file": {"fn": read_file, "params": {"path": "str"}},
    "write_file": {"fn": write_file, "params": {"path": "str", "content": "str"}},
    "run_command": {"fn": run_command, "params": {"cmd": "str"}},
    "search_codebase": {"fn": search_codebase, "params": {"pattern": "str", "directory": "str"}},
}

# ─── LLM Call ────────────────────────────────────────────────────

def call_llm(messages: list) -> dict:
    import anthropic
    client = anthropic.Anthropic(api_key=API_KEY)

    tool_defs = [
        {
            "name": name,
            "description": f"Tool: {name}",
            "input_schema": {
                "type": "object",
                "properties": {k: {"type": "string"} for k in spec["params"]},
                "required": list(spec["params"].keys()),
            },
        }
        for name, spec in TOOLS.items()
    ]

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=messages,
        tools=tool_defs,
    )
    return response


SYSTEM_PROMPT = """You are a coding agent. You accomplish tasks by calling tools iteratively.
Rules:
- Use tools to read, write, and execute code.
- After writing code, run tests to verify.
- Make minimal changes. Do not refactor unrelated code.
- When the task is complete, reply with a summary and stop calling tools.
"""

# ─── Agentic Loop ────────────────────────────────────────────────

def run_agent(task: str):
    messages = [{"role": "user", "content": task}]

    for i in range(MAX_ITERATIONS):
        print(f"\n{'='*50}\nIteration {i+1}\n{'='*50}")

        response = call_llm(messages)

        # Append assistant's response to conversation
        messages.append({"role": "assistant", "content": response.content})

        # Check if agent is done (no tool_use blocks)
        tool_uses = [b for b in response.content if b.type == "tool_use"]
        if not tool_uses:
            # Agent finished — extract text summary
            text = "".join(b.text for b in response.content if b.type == "text")
            print(f"\n✅ Done: {text}")
            break

        # Execute each tool call
        tool_results = []
        for tu in tool_uses:
            name = tu.name
            args = tu.input
            print(f"  🔧 {name}({json.dumps(args, indent=2)[:200]})")

            if name not in TOOLS:
                result = f"Unknown tool: {name}"
            else:
                result = TOOLS[name]["fn"](**args)
                print(f"  → {result[:150]}...")

            tool_results.append({
                "type": "tool_result",
                "tool_use_id": tu.id,
                "content": result,
            })

        messages.append({"role": "user", "content": tool_results})

    else:
        print("⚠️  Max iterations reached.")


# ─── Entry Point ─────────────────────────────────────────────────

if __name__ == "__main__":
    task = input("Task: ")
    run_agent(task)   
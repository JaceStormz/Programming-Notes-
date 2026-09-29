# Gautam Rao
# 9/27/2026
# Python version 3.13

"""
RegexScraper.py

Purpose:
    Extract the table, rows, headers, and cells from the supplied Planets.html
    file using focused regular expressions. This is an assignment-specific
    parser for simple table markup, not a general-purpose HTML parser.

"""

import re
from collections import defaultdict
from pathlib import Path


class RegexScraper:
    """Extract headers and column values from simple HTML table markup."""

    # Notebook Section: HTML Tag Recognition (Regex.py lines 157-171)
    # Used in: __init__()
    # Changes:
    #   - Use specific patterns for tables, rows, and cells instead of one general HTML tag pattern.
    #   - Compile the patterns once per scraper object instead of compiling them every time a parsing method runs.
    #   - Store the original HTML and parsed data inside the object.
    # Design Factors Executed:
    #   - Encapsulation: _html_text and _table_data store the object's internal data, which callers access through the class methods.
    #   - Robustness: isinstance() checks the input type right away and raises a clear TypeError if the input is invalid, instead of failing later during parsing.
    #   - Scalability: These reusable patterns avoid recompiling the same regex for every row or cell.
    def __init__(self, html_text):
        if not isinstance(html_text, str):
            raise TypeError("html_text must be a string")

        self._html_text = html_text
        self._table_data = defaultdict(list)

        # Notebook Section: HTML Tag Recognition (Regex.py lines 157-171)
        # Used in: __init__() / ExtractTable()
        # Changes:
        #   - Match only the <table> tag and its contents.
        #   - \b ensures <table> matches without accidentally matching tags like <tabledata>.
        #   - [^>]* allows opening tags to have optional attributes.
        #   - (.*?) captures the table's contents, and DOTALL allows it to match across multiple lines in Planets.html.
        # Design Factors Executed:
        #   - Modularity: Extracts the table separately from rows and cells using its own pattern and method.
        #   - Robustness: The specific table pattern avoids unrelated tags, and ExtractTable() clearly reports when no table is found.
        #   - Scalability: the compiled pattern is reusable across parses.
        self._table_re = re.compile(
            r"<table\b[^>]*>(.*?)</table\s*>",
            re.IGNORECASE | re.DOTALL
        )

        # Notebook Section: Greedy vs Non-Greedy Matching (Regex.py lines 174-199)
        # Used in: _ExtractRows()
        # Changes:
        #   - Apply non-greedy matching to each tr element inside the table.
        #   - Capture row contents without the opening/closing tr tags.
        self._row_re = re.compile(
            r"<tr\b[^>]*>(.*?)</tr\s*>",
            re.IGNORECASE | re.DOTALL
        )

        # Notebook Section: HTML Tag Recognition and capture groups
        # (Regex.py lines 157-171)
        # Used in: _ExtractCells()
        # Changes:
        #   - Capture the th or td tag in group 1 and its contents in group 2.
        #   - \1 ensures the closing tag matches the opening tag.
        self._cell_re = re.compile(
            r"<(th|td)\b[^>]*>(.*?)</\1\s*>",
            re.IGNORECASE | re.DOTALL
        )

        # Notebook Section: Applying Regular Expressions / tag recognition
        # Used in: _TrimText()
        # Changes:
        # - Remove simple inline tags inside a cell.
        # - Keep the superscript("<sup>"") text next to the surrounding text without adding spaces. For example, 10<sup>24</sup> kg becomes 1024 kg, not 10 24 kg.
        self._inline_tag_re = re.compile(r"<[^>]+>", re.DOTALL)

    # Notebook Section: HTML Tag Recognition (Regex.py lines 157-171)
    # Used in: ExtractTable()
    # Changes:
    #   - Use the table-specific compiled expression from __init__.
    #   - Raise a clear error if the supplied HTML has no table.
    # Design Factors Executed:
    #   - Modularity: this method returns only the table's inner HTML.
    #   - Robustness: a missing table produces a descriptive ValueError.
    def ExtractTable(self):
        match = self._table_re.search(self._html_text)
        if not match:
            raise ValueError("No table element was found in the supplied HTML")
        return match.group(1)

    # Notebook Section: Greedy vs Non-Greedy Matching (Regex.py lines 174-199)
    # Used in: _ExtractRows()
    # Changes:
    #   - Returns the contents of each tr element in the order they appear in the source.
    #   - Use the compiled pattern repeatedly without recompiling it each time.
    # Design Factors Executed:
    #   - Modularity: Extracts rows separately from the table and cell parsing.
    #   - Scalability: findall() finds all rows in the order they appear in the source, no matter how many there are.
    def _ExtractRows(self, table_html):
        return self._row_re.findall(table_html)

    # Notebook Section: HTML Tag Recognition (Regex.py lines 157-171)
    # Used in: _ExtractCells()
    # Changes:
    #   - Returns matching opening and closing tags for both th and td elements.
    #   - The backreference ensures the closing tag matches the opening tag.
    # Design Factors Executed:
    #   - Modularity: Extracts cell data in a separate method that can be reused.
    #   - Robustness: The backreference ensures that opening and closing tags match: th with th or td with td.
    #   - Scalability: Uses the same pattern for every cell without relying on specific column names or a fixed number of cells.
    def _ExtractCells(self, row_html):
        return self._cell_re.findall(row_html)

    # Notebook Section: Applying Regular Expressions / tag recognition
    # Used in: _TrimText()
    # Changes:
    #   - Remove simple HTML tags, then clean up extra spaces and line breaks.
    #   - Removing the tags keeps the superscript text next to the surrounding text, so 10<sup>24</sup> becomes 1024 without adding a space.
    #   - Consistent whitespace keeps all stored values clean and uniform.
    # Design Factors Executed:
    #   - Modularity: Cleans up text in one place so all headers and cells follow the same trimming rules.
    #   - Robustness: Keeps whitespace consistent, even when the source has line breaks or extra spaces.
    def _TrimText(self, cell_html):
        no_tags = self._inline_tag_re.sub("", cell_html)
        return " ".join(no_tags.split()).strip()

    # Notebook Section: findall() and capture groups (Regex.py lines 197-200)
    # Used in: ParseTable()
    # Changes:
    #   - Coordinate the extraction of the table, rows, headers, and cell data.
    #   - Use cleaned header names as consistent keys to access each column.
    #   - Add a suffix to duplicate header names so they don't overwrite each other in the dictionary.
    #   - Fill missing cells with "" and store extra cells using cell_N keys to avoid losing data from irregular rows.
    #   - Use defaultdict(list) to automatically group values into lists, as shown in the DefaultDict.ipynb examples.
    # Design Factors Executed:
    #   - Modularity: This method calls the helper methods to handle the work instead of repeating their regex and cleanup code.
    #   - Robustness: Checks for missing rows or headers, fills empty cells with "", and keeps extra cells using cell_N keys.
    #   - Scalability: Loops through the rows and headers it finds instead of relying on a fixed number of planets or columns.
    #   - Encapsulation: Stores the parsed results in _table_data and makes them available through the class interface.
    def ParseTable(self):
        table_html = self.ExtractTable()
        rows = self._ExtractRows(table_html)
        if not rows:
            raise ValueError("The table element contains no rows")

        headers = []
        data_rows = []

        for row_html in rows:
            cells = self._ExtractCells(row_html)
            if not cells:
                continue

            tags = [tag.lower() for tag, _ in cells]
            values = [self._TrimText(content) for _, content in cells]

            if not headers and "th" in tags:
                headers = values
            else:
                data_rows.append(values)

        if not headers:
            raise ValueError("No header row containing <th> cells was found")

        keys = []
        seen = defaultdict(int)
        for index, header in enumerate(headers, start=1):
            base = header if header else f"column_{index}"
            seen[base] += 1
            key = base if seen[base] == 1 else f"{base}_{seen[base]}"
            keys.append(key)

        results = defaultdict(list)
        for values in data_rows:
            for index, key in enumerate(keys):
                value = values[index] if index < len(values) else ""
                results[key].append(value)

            for index in range(len(keys), len(values)):
                results[f"cell_{index + 1}"].append(values[index])

        self._table_data = results
        return headers, results

    # Notebook Section: DefaultDict.ipynb grouping / missing-key behavior
    # Used in: GetColumn()
    # Changes:
    #   - Return a copy of the requested column.
    #   - If a key doesn't exist, return an empty list without adding that key to the dictionary..
    # Design Factors Executed:
    #   - Encapsulation:Returns a copy of the list so changes made by the caller don't affect the original list stored internally.
    #   - Robustness: unknown keys safely return an empty list.
    #   - Modularity: Provides a simple, consistent way to get a column without showing how the data is parsed internally.
    def GetColumn(self, key):
        return list(self._table_data.get(key, []))


if __name__ == "__main__":
    # Read only the provided local Planets.html file without accessing the internet.
    html_path = Path(__file__).with_name("Planets.html")
    html = html_path.read_text(encoding="utf-8")

    scraper = RegexScraper(html)
    headers, data = scraper.ParseTable()

    print("Headers:")
    print(headers)
    print("\nExtracted columns:")
    for header in data:
        print(f"{header}: {data[header]}")

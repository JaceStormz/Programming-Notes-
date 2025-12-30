const baseUrl = "http://localhost:3000";

document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.getElementById("registerForm");
  const loginForm = document.getElementById("loginForm");

  if (registerForm) {
    registerForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const data = {
        username: e.target.username.value,
        password: e.target.password.value,
      };
      const res = await fetch(`${baseUrl}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      const msg = await res.json();
      alert(msg.message);
      if (res.ok) window.location.href = "login.html";
    });
  }

  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const data = {
        username: e.target.username.value,
        password: e.target.password.value,
      };
      const res = await fetch(`${baseUrl}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      const msg = await res.json();
      alert(msg.message);
      if (res.ok) {
        localStorage.setItem("username", msg.username);
        window.location.href = "index.html";
      }
    });
  }
});
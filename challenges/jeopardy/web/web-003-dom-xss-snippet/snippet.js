const params = new URLSearchParams(window.location.search);
const name = params.get("name") || "guest";
document.getElementById("welcome").innerHTML = `Welcome ${name}`;

window.addEventListener("message", (event) => {
  document.getElementById("status").innerHTML = event.data.message;
});

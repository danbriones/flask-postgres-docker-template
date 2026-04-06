// Auto-dismiss Bootstrap alerts after 5 seconds
document.addEventListener("DOMContentLoaded", function () {
  const alerts = document.querySelectorAll(".alert");

  alerts.forEach(function (alert) {
    setTimeout(function () {
      // Use Bootstrap's built-in styling to fade out
      alert.classList.remove("show");
      alert.classList.add("fade");

      // Remove from DOM after transition completes
      setTimeout(() => {
        alert.remove();
      }, 500);
    }, 5000); // 5000ms = 5 seconds
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const notice = document.querySelector(".safety-notice");
  const closeButton = notice && notice.querySelector(".safety-notice__close");

  if (notice && closeButton) {
    closeButton.addEventListener("click", () => {
      notice.hidden = true;
    });
  }
});

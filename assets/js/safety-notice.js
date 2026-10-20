document.addEventListener("DOMContentLoaded", () => {
  const notice = document.querySelector(".safety-notice");

  if (!notice) {
    return;
  }

  notice.hidden = false;

  const closeButton = notice.querySelector(".safety-notice__close");

  if (closeButton) {
    closeButton.addEventListener("click", () => {
      notice.hidden = true;
    });
  }
});

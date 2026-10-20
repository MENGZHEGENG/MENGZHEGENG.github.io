document.addEventListener("DOMContentLoaded", () => {
  const notice = document.querySelector(".safety-notice");

  if (!notice) {
    return;
  }

  const disabledUntil = Date.parse(notice.dataset.disabledUntil || "2026-10-20T15:09:47Z");
  const restoreNotice = () => {
    const remaining = disabledUntil - Date.now();

    if (Number.isFinite(disabledUntil) && remaining > 0) {
      notice.hidden = true;
      window.setTimeout(restoreNotice, remaining);
      return;
    }

    notice.hidden = false;
  };

  restoreNotice();

  const closeButton = notice.querySelector(".safety-notice__close");

  if (closeButton) {
    closeButton.addEventListener("click", () => {
      notice.hidden = true;
    });
  }
});

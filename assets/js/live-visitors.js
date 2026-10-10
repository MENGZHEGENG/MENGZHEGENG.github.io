(() => {
  const counter = document.querySelector("[data-live-visitors]");
  if (!counter) return;

  const hash = counter.dataset.hash;
  const count = counter.querySelector("[data-live-visitors-count]");
  const status = counter.querySelector("[data-live-visitors-status]");
  if (!hash || !count || !status) {
    if (status) status.textContent = "Live count temporarily unavailable.";
    return;
  }

  const endpoint = new URL("https://statable.com/api/widget/realtime");
  endpoint.searchParams.set("hash", hash);
  let refreshTimer = null;
  let requestInFlight = false;

  async function refreshCount() {
    if (document.hidden || requestInFlight) return;
    requestInFlight = true;
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 15_000);

    try {
      const response = await fetch(endpoint, {
        cache: "no-store",
        credentials: "omit",
        signal: controller.signal,
      });
      if (!response.ok) throw new Error("Live visitor request failed.");

      const data = await response.json();
      if (!Number.isSafeInteger(data.v) || data.v < 0) {
        throw new Error("Live visitor response was invalid.");
      }

      count.textContent = data.v.toLocaleString();
      status.textContent = "Refreshes every minute.";
    } catch {
      status.textContent = "Live count temporarily unavailable.";
    } finally {
      window.clearTimeout(timeout);
      requestInFlight = false;
    }
  }

  function startRefreshing() {
    if (document.hidden || refreshTimer !== null) return;
    refreshCount();
    refreshTimer = window.setInterval(refreshCount, 60_000);
  }

  function stopRefreshing() {
    if (refreshTimer === null) return;
    window.clearInterval(refreshTimer);
    refreshTimer = null;
  }

  document.addEventListener("visibilitychange", () => {
    if (document.hidden) stopRefreshing();
    else startRefreshing();
  });

  startRefreshing();
})();

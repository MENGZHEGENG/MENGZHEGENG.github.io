(function () {
  "use strict";

  const counter = document.querySelector("[data-visitor-counter]");
  if (!counter) return;

  const value = counter.querySelector("[data-visitor-count-value]");
  const label = counter.querySelector("[data-visitor-count-label]");
  const hash = counter.dataset.statableHash;
  if (!value || !label || !hash) return;

  const endpoint = new URL("https://statable.com/api/widget/realtime");
  endpoint.searchParams.set("hash", hash);

  fetch(endpoint.toString(), {
    method: "GET",
    cache: "no-store",
    credentials: "omit",
    referrerPolicy: "no-referrer",
    headers: { Accept: "application/json" }
  })
    .then(function (response) {
      if (!response.ok) throw new Error("Visitor count request failed");
      return response.json();
    })
    .then(function (data) {
      if (!Number.isSafeInteger(data.v) || data.v < 0) {
        throw new Error("Visitor count response was invalid");
      }

      value.textContent = new Intl.NumberFormat().format(data.v);
      label.textContent = data.v === 1
        ? "visitor active in the last 30 minutes"
        : "visitors active in the last 30 minutes";
    })
    .catch(function () {
      value.textContent = "...";
      label.textContent = "Live visitor count is temporarily unavailable";
    });
})();

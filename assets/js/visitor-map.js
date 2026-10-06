(function () {
  "use strict";

  const map = document.getElementById("visitor-map");
  if (!map) return;

  const widgetUrl = "https://statable.com/js/G4H6CB0Fb6/mw.js";
  const darkPreference = window.matchMedia("(prefers-color-scheme: dark)");
  let activeTheme = null;

  function currentTheme() {
    const savedTheme = window.localStorage.getItem("theme");
    if (savedTheme === "dark" || savedTheme === "light") return savedTheme;
    return darkPreference.matches ? "dark" : "light";
  }

  function renderMap() {
    const theme = currentTheme();
    if (theme === activeTheme) return;
    activeTheme = theme;

    const script = document.createElement("script");
    script.src = widgetUrl;
    script.async = true;
    script.dataset.id = "3386330";
    script.dataset.theme = theme;
    script.dataset.period = "7d";
    script.dataset.displayMode = "heatmap";
    script.dataset.showStats = "true";
    script.dataset.outerRadius = "8";
    script.dataset.primaryColor = theme === "dark" ? "#80ded0" : "#176b65";
    script.dataset.oceanColor = theme === "dark" ? "#15201e" : "#f4f7f6";
    script.dataset.statsTextColor = theme === "dark" ? "#a6b9b4" : "#53635f";
    script.onerror = function () {
      if (activeTheme !== theme) return;
      const status = document.createElement("p");
      status.className = "visitor-counter__map-status";
      status.textContent = "The visitor map is temporarily unavailable.";
      map.replaceChildren(status);
    };

    map.replaceChildren(script);
  }

  renderMap();

  const themeObserver = new MutationObserver(renderMap);
  themeObserver.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["data-theme"]
  });

  darkPreference.addEventListener("change", function () {
    const savedTheme = window.localStorage.getItem("theme");
    if (savedTheme !== "dark" && savedTheme !== "light") renderMap();
  });
})();

const timeline = document.querySelector(".publication-filters");

if (timeline) {
  const filters = [...timeline.querySelectorAll("[data-publication-filter]")];
  const publications = [...document.querySelectorAll(".author-led-publication")];
  const status = document.querySelector(".publication-filter-status");

  filters.forEach((filter) => {
    filter.addEventListener("click", () => {
      const selectedTheme = filter.dataset.publicationFilter;
      let visibleCount = 0;

      filters.forEach((button) => {
        const isSelected = button === filter;
        button.classList.toggle("is-active", isSelected);
        button.setAttribute("aria-pressed", String(isSelected));
      });

      publications.forEach((publication) => {
        const isVisible = selectedTheme === "all" || publication.dataset.publicationTheme === selectedTheme;
        publication.hidden = !isVisible;
        if (isVisible) visibleCount += 1;
      });

      if (status) {
        status.textContent = `${visibleCount} publication${visibleCount === 1 ? "" : "s"}`;
      }
    });
  });
}

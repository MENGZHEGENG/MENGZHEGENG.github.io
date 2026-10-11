const citationPanels = document.querySelectorAll(".publication-cite[data-citation-title]");

function parseCitationAuthor(rawAuthor) {
  const name = rawAuthor.replace(/\*/g, "").replace(/\s+/g, " ").trim();

  if (!name || /^et al\.?$/i.test(name)) {
    return { etAl: true };
  }

  const parts = name.split(" ");
  const family = parts.pop();
  const givenParts = parts;
  const initials = givenParts.map((part) => part
    .split("-")
    .map((segment) => `${segment.replace(/\./g, "").charAt(0).toUpperCase()}.`)
    .join("-"));
  const initialString = initials.join(" ");

  return {
    family,
    initials: initialString,
    apa: initialString ? `${family}, ${initialString}` : family,
    ieee: initialString ? `${initialString} ${family}` : family,
    bibtex: givenParts.length ? `${family}, ${givenParts.join(" ")}` : family,
  };
}

function citationAuthors(rawAuthors) {
  return rawAuthors
    .split(",")
    .map((author) => parseCitationAuthor(author))
    .filter((author, index, authors) => !author.etAl || index === authors.length - 1);
}

function apaAuthorList(authors) {
  const knownAuthors = authors.filter((author) => !author.etAl);
  const hasEtAl = authors.some((author) => author.etAl);
  let formattedAuthors;

  if (hasEtAl) {
    formattedAuthors = [...knownAuthors.map((author) => author.apa), "et al."].join(", ");
  } else if (knownAuthors.length > 20) {
    formattedAuthors = `${knownAuthors.slice(0, 19).map((author) => author.apa).join(", ")}, . . . ${knownAuthors.at(-1).apa}`;
  } else if (knownAuthors.length < 2) {
    formattedAuthors = knownAuthors[0]?.apa ?? "";
  } else {
    formattedAuthors = `${knownAuthors.slice(0, -1).map((author) => author.apa).join(", ")}, & ${knownAuthors.at(-1).apa}`;
  }

  return formattedAuthors;
}

function ieeeAuthorList(authors) {
  const knownAuthors = authors.filter((author) => !author.etAl).map((author) => author.ieee);
  if (authors.some((author) => author.etAl)) return [...knownAuthors, "et al."].join(", ");
  if (knownAuthors.length < 2) return knownAuthors[0] ?? "";
  if (knownAuthors.length === 2) return `${knownAuthors[0]} and ${knownAuthors[1]}`;
  return `${knownAuthors.slice(0, -1).join(", ")}, and ${knownAuthors.at(-1)}`;
}

function normalizedDoi(rawDoi) {
  return rawDoi.replace(/^https?:\/\/(?:dx\.)?doi\.org\//i, "").trim();
}

function bibtexEscape(value) {
  return value
    .replace(/\\/g, "\\textbackslash{}")
    .replace(/([{}])/g, "\\$1")
    .replace(/([#$%&_])/g, "\\$1")
    .replace(/~/g, "\\textasciitilde{}")
    .replace(/\^/g, "\\textasciicircum{}");
}

function bibtexKey(author, year, title) {
  const family = author.find((entry) => !entry.etAl)?.family ?? "geng";
  const titleSlug = title.normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "")
    .slice(0, 28);
  const authorSlug = family.normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "") || "author";

  return `${authorSlug}${year}${titleSlug}`;
}

function bibtexType(venue) {
  const normalizedVenue = venue.toLowerCase();
  if (normalizedVenue.includes("arxiv") || normalizedVenue.includes("submitted")) return "misc";
  if (/transactions|journal|computing surveys|computer speech & language|ieee intelligent systems/.test(normalizedVenue)) return "article";
  return "inproceedings";
}

function bibtexCitation(metadata, authors, doi, url) {
  const type = bibtexType(metadata.venue);
  const venueField = type === "article" ? "journal" : "booktitle";
  const bibtexAuthors = authors.map((author) => author.etAl ? "others" : author.bibtex).join(" and ");
  const fields = [
    `  author = {${bibtexEscape(bibtexAuthors)}},`,
    `  title = {{${bibtexEscape(metadata.title)}}},`,
  ];

  if (metadata.venue) {
    fields.push(`  ${type === "misc" ? "howpublished" : venueField} = {${bibtexEscape(metadata.venue)}},`);
  }
  fields.push(`  year = {${bibtexEscape(metadata.year)}},`);
  if (doi) fields.push(`  doi = {${bibtexEscape(doi)}},`);
  if (url) fields.push(`  url = {${bibtexEscape(url)}}`);

  return `@${type}{${bibtexKey(authors, metadata.year, metadata.title)},\n${fields.join("\n")}\n}`;
}

function citationFor(panel, format) {
  const metadata = panel.dataset;
  const authors = citationAuthors(metadata.citationAuthors ?? "");
  const doi = normalizedDoi(metadata.citationDoi ?? "");
  const url = metadata.citationUrl ?? "";
  const venue = metadata.citationVenue ?? "";
  const year = metadata.citationYear ?? "";
  const title = metadata.citationTitle ?? "";

  if (format === "apa") {
    const authorText = apaAuthorList(authors);
    const locator = doi ? `https://doi.org/${doi}` : url;
    return `${authorText} (${year}). ${title}. ${venue}.${locator ? ` ${locator}` : ""}`;
  }

  if (format === "ieee") {
    const authorText = ieeeAuthorList(authors);
    const locator = doi ? `doi: ${doi}` : url ? `Available: ${url}` : "";
    return `${authorText}, “${title},” ${venue}, ${year}.${locator ? ` ${locator}` : ""}`;
  }

  return bibtexCitation({ title, venue, year }, authors, doi, url);
}

function copyFallback(text, output) {
  const range = document.createRange();
  range.selectNodeContents(output);
  const selection = window.getSelection();
  selection.removeAllRanges();
  selection.addRange(range);
  const copied = document.execCommand("copy");
  selection.removeAllRanges();
  return copied;
}

citationPanels.forEach((panel) => {
  const formatSelect = panel.querySelector("[data-citation-format]");
  const output = panel.querySelector("[data-citation-output]");
  const copyButton = panel.querySelector("[data-citation-copy]");
  const status = panel.querySelector("[data-citation-status]");

  const refreshCitation = () => {
    output.textContent = citationFor(panel, formatSelect.value);
    status.textContent = "";
  };

  formatSelect.addEventListener("change", refreshCitation);
  refreshCitation();

  copyButton.addEventListener("click", async () => {
    const text = output.textContent;
    try {
      if (navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(text);
      } else if (!copyFallback(text, output)) {
        throw new Error("Clipboard access is unavailable");
      }
      status.textContent = `${formatSelect.options[formatSelect.selectedIndex].text} citation copied.`;
    } catch {
      output.focus();
      status.textContent = "Select the citation above and copy it.";
    }
  });
});

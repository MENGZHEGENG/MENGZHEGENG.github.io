const SITE_HOST = "mengzhegeng.com";
const LEGACY_HOST = "www.mengzhegeng.com";
const CANADA_PAGE = "/_canada/index.html";

const CANADA_ASSETS = new Set([
  "/assets/css/canada-simple.css",
  "/assets/js/safety-notice.js",
  "/images/favicon.svg",
  "/images/mengzhe-geng.jpg",
]);

function privatePage(response, robots = false) {
  const headers = new Headers(response.headers);
  headers.set("Cache-Control", "private, no-store");
  headers.set("Vary", "CF-IPCountry");
  if (robots) headers.set("X-Robots-Tag", "noindex, nofollow");
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}

function notFound() {
  return new Response("Not found", {
    status: 404,
    headers: { "Cache-Control": "private, no-store", "X-Robots-Tag": "noindex" },
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();

    if (host === LEGACY_HOST) {
      url.hostname = SITE_HOST;
      return Response.redirect(url.toString(), 308);
    }

    if (host !== SITE_HOST || !["GET", "HEAD"].includes(request.method)) {
      return notFound();
    }

    if (url.pathname === CANADA_PAGE || url.pathname.startsWith("/_canada/")) {
      return notFound();
    }

    if (request.cf?.country !== "CA") {
      return env.ASSETS.fetch(request);
    }

    if (url.pathname === "/robots.txt") {
      return new Response("User-agent: *\nDisallow: /\n", {
        headers: {
          "Cache-Control": "private, no-store",
          "Content-Type": "text/plain; charset=utf-8",
          "X-Robots-Tag": "noindex, nofollow",
          Vary: "CF-IPCountry",
        },
      });
    }

    if (url.pathname === "/" || url.pathname === "/index.html") {
      const simpleUrl = new URL(CANADA_PAGE, url);
      const response = await env.ASSETS.fetch(new Request(simpleUrl, request));
      return privatePage(response, true);
    }

    if (CANADA_ASSETS.has(url.pathname)) {
      return env.ASSETS.fetch(request);
    }

    return notFound();
  },
};

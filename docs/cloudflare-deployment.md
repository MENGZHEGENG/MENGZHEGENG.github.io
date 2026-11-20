# Cloudflare deployment setup

The full Jekyll build is deployed to a Cloudflare Worker with static assets. The Worker serves the compact shared profile to Canadian IPs and the full site elsewhere. The legacy `mengzhegeng.github.io` Pages site contains only a redirect to `mengzhegeng.com`.

## One-time account setup

1. Reuse the existing Worker named `engzhegeng-academic-site` in the `mengzhegeng.com` Cloudflare account. The source configuration uses that exact service name; do not create a duplicate Worker.
2. In the Worker's **Settings → Domains & Routes**, add custom domains `mengzhegeng.com` and `www.mengzhegeng.com`. Cloudflare will create the DNS records and certificates. The Worker redirects `www` to the apex domain. Check that neither hostname has a conflicting CNAME before adding the custom domain. See [Cloudflare custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/).
3. Create an API token for GitHub Actions with **Workers Editor** access scoped only to the `engzhegeng-academic-site` Worker. Because the custom domains are attached in the dashboard, the deployment token does not need route, DNS, account-wide Admin, billing, account-settings, or user permissions. See [Workers roles and permissions](https://developers.cloudflare.com/workers/authorization/workers/).
4. In the public website repository's **Settings → Secrets and variables → Actions**, add:
   - Repository secret `CLOUDFLARE_API_TOKEN`: paste the token directly into GitHub's secret form. Do not send it in chat or commit it.
   - Repository variable `CLOUDFLARE_ACCOUNT_ID`: enter the Cloudflare account ID shown in the account overview.
5. Once the secret and variable are saved, merge the website branch to `main`. The `pages.yml` workflow deploys the Worker first and then replaces the old GitHub Pages site with the redirect. The visitor workflow rebuilds and deploys the current site every 10 minutes.

The compact Canadian page shares the name/photo include, safety notice, and visitor-count include with the full site. The Worker only allows the compact page and its stylesheet, photo, favicon, and banner script for Canadian requests; other content paths return 404. It disables `workers.dev` and version-preview URLs, and sends the country-specific HTML with `private, no-store` to prevent one region's page from being cached for another.

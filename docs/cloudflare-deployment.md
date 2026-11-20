# Cloudflare deployment setup

The full Jekyll build is deployed to a Cloudflare Worker with static assets. The Worker serves the compact shared profile to Canadian IPs and the full site elsewhere. The legacy `mengzhegeng.github.io` Pages site contains only a redirect to `mengzhegeng.com`.

## One-time account setup

1. Reuse the existing Worker named `engzhegeng-academic-site` in the `mengzhegeng.com` Cloudflare account. The source configuration uses that exact service name; do not create a duplicate Worker.
2. Create a Cloudflare API token for GitHub Actions with **Workers Editor** access scoped only to this Worker. The custom domains are configured in the dashboard, so the deployment token does not need route, DNS, account-wide Admin, billing, account-settings, or user permissions. See [Workers roles and permissions](https://developers.cloudflare.com/workers/authorization/workers/) and [Cloudflare's GitHub Actions guide](https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/).
3. In the public website repository's **Settings → Secrets and variables → Actions**, add:
   - Repository secret `CLOUDFLARE_API_TOKEN`: paste the token directly into GitHub's secret form. Do not send it in chat or commit it.
   - Repository variable `CLOUDFLARE_ACCOUNT_ID`: enter the Cloudflare account ID shown in the account overview.
4. Dispatch `pages.yml` from the website branch with `deploy_legacy_redirect` disabled. This deploys the Worker while leaving the current GitHub Pages content in place.
5. After the Worker code is deployed, add `mengzhegeng.com` and `www.mengzhegeng.com` under its **Settings → Domains & Routes**. Cloudflare creates the DNS records and certificates. The Worker redirects `www` to the apex domain. Check for conflicting CNAME records first. See [Cloudflare custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/).
6. Verify the custom domain, then merge the website branch to `main`. The `pages.yml` workflow deploys the Worker and replaces the old GitHub Pages site with the redirect. The visitor workflow rebuilds and deploys the current site every 10 minutes.

The compact Canadian page shares the name/photo include, safety notice, and visitor-count include with the full site. The Worker only allows the compact page and its stylesheet, photo, favicon, and banner script for Canadian requests; other content paths return 404. It disables `workers.dev` and version-preview URLs, and sends the country-specific HTML with `private, no-store` to prevent one region's page from being cached for another.


# Binance Liquidation Monitor — Lite HTML Dashboard

Single-file HTML dashboard you can open directly in a browser, or host on any static hosting (GitHub Pages, Vercel static, Nginx).

## How to use

1. Put this file anywhere and open it in a browser: `liquidation-dashboard.html`.
2. By default, it will try to fetch from `/api/...` endpoints. If your Flask backend exposes endpoints at the root (e.g. `/status`), pass a custom base:
   - Example: `file:///.../liquidation-dashboard.html?apiBase=http://localhost:8080`
   - Then it will call:
     - `GET http://localhost:8080/status`
     - `GET http://localhost:8080/liquidations`
     - `GET http://localhost:8080/symbols`
3. If the API is unreachable, it shows mock data and a "Mock Mode" badge so the UI is still visible.

## Recommended backend endpoints

Adapt these to your current API. From your docs, typical endpoints are:
- `/api/status` or `/status`
- `/api/liquidations` or `/liquidations`
- `/api/symbols`

If yours are `/api/...`, launch with `?apiBase=http://host:port/api`. If `/...`, use `?apiBase=http://host:port`.

## Deploy

- **GitHub Pages**: Commit this HTML file to the repo (e.g., `docs/`), enable Pages.
- **Vercel**: Create a project from your repo and serve it as static.
- **Docker/Flask**: Serve as a static file alongside your API if desired.

Generated: 2025-08-21T07:20:25.643154Z

# Binance Liquidation Monitor

Monorepo berisi:
- **backend/**: Flask API sederhana (`/status`, `/liquidations`, `/symbols`) siap jalan lokal atau Docker.
- **docs/**: semua dokumentasi yang kamu upload + **dashboard HTML satu file** untuk UI cepat.

## Quick Start (Local)

```bash
# 1) Jalankan backend (butuh Python 3.11+)
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py  # runs at http://localhost:8080

# 2) Buka dashboard (file HTML)
# Klik dua kali: docs/liquidation-dashboard.html
# atau dengan custom API base:
# file:///.../liquidation-dashboard.html?apiBase=http://localhost:8080
```

## Quick Start (Docker)

```bash
docker compose up --build
# Backend di http://localhost:8080
# Buka docs/liquidation-dashboard.html dengan ?apiBase=http://localhost:8080
```

## Struktur
```
binance-liquidation-monitor-repo/
├─ backend/
│  ├─ app.py
│  ├─ requirements.txt
│  ├─ Dockerfile
│  └─ run.sh
├─ docs/
│  ├─ liquidation-dashboard.html
│  ├─ README-lite-dashboard.md
│  ├─ (semua dokumen yang kamu upload)
└─ docker-compose.yml
```

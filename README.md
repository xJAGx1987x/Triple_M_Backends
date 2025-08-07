# Triple M Backends

This repository contains modular backend services built for the Triple M Studios web projects. Each subdirectory is a standalone FastAPI-based backend that can be independently deployed or integrated into larger systems.

## Structure

TRIPLE_M_BACKENDS/

├── lyrics-search/       # Backend for the synced lyrics search tool (FastAPI + syncedlyrics)

├── another-backend/     # (Placeholder for additional services)

└── .gitignore           # Ignores virtual environments and cache files

## Projects

### 🎵 Lyrics Search

A FastAPI-powered API that uses [`syncedlyrics`](https://github.com/moehmeni/syncedlyrics) to fetch time-synced lyrics from multiple sources. This service powers the `/projects/lyrics-search/` frontend.

- Endpoint: `GET /lyrics?artist=...&title=...`
- Dependencies: `syncedlyrics`, `FastAPI`, `uvicorn`
- Deployed using: Render / Replit / (your platform here)

## Development Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/TripleMStudio/TRIPLE_M_BACKENDS.git
   cd TRIPLE_M_BACKENDS/lyrics-search
   ```

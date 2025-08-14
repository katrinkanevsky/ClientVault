# ClientVault

Secure, simple client management for law firms.  
Built with **Flask**, **SQLite** (local) / **PostgreSQL** (production ready), and **Tailwind CSS**.

## Features
- Per-firm data isolation (each firm sees only its clients)
- Login / signup for firms
- Add clients, view all clients, and search by multiple fields
- Clean Tailwind UI (compiled to a single `static/tw.css`)

## Tech Stack
- **Backend**: Flask (Python)
- **DB (local)**: SQLite (single file)
- **DB (production)**: PostgreSQL (recommended)
- **Frontend**: Tailwind CSS (compiled, no CDN in production)
- **Server (production)**: Gunicorn (WSGI)

## Repository Structure

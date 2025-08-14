# ClientVault

ClientVault is a simple, secure web app for law firms to store and search client records.  
Each firm can log in and access only its own data.

---

## How to use this document
- **Where to paste:** Save this entire file as `README.md` in the **project root** (same folder as `app.py`).
- **Who this is for:** Anyone who wants to run ClientVault on their own computer.

---

## Quick Start (Local, SQLite)

Follow these steps in order. You only need Python. Node.js is **not** required unless you plan to change the CSS.

### 1) Get the code
If you already have the folder on your computer, skip this.
```bash
git clone https://github.com/<your-user>/ClientVault.git
cd ClientVault
```

### 2) Create and activate a virtual environment, then install Python packages
```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows (PowerShell)
# .\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 3) Initialize the database (SQLite)
Run setup_database.py in your terminal to set up the database
```bash
# 
python setup_database.py

# 
```

### 4) Secret key (sessions)
- Locally, the app already has a **development fallback** and will run without any extra steps.
- If you ever see “secret key not set”, set one like this:

```bash
# macOS / Linux
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"

# Windows (PowerShell)
# setx SECRET_KEY "(python -c \"import secrets; print(secrets.token_hex(32))\")"
```

The app reads it in `app.py` like this (already in the code):
```python
import os
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")
```

### 5) Run the app
```bash
python app.py
# Open http://127.0.0.1:5000 in your browser
```

### 6) Stopping and cleaning up
- Stop the server: press `Ctrl+C` in the terminal.
- Deactivate the virtual environment: `deactivate`

---

## Optional (Only if you change the UI/CSS)

This project uses Tailwind CSS, but the **compiled CSS file** `static/tw.css` is already included.  
You do **not** need Node.js unless you want to change styles.

- If you edit styles in `static/src/tailwind.css`, rebuild the CSS:
```bash
# install Node packages once
npm install

# build a minified CSS for production
./node_modules/.bin/tailwindcss -i ./static/src/tailwind.css -o ./static/tw.css --minify
```

---

## Project Structure (what files are where)
```
ClientVault/
├─ app.py
├─ requirements.txt
├─ Procfile                       # used by cloud hosts (gunicorn start command)
├─ tailwind.config.js
├─ package.json
├─ package-lock.json
├─ templates/                     # all HTML templates (base.html, home.html, etc.)
├─ static/
│  └─ tw.css                      # compiled Tailwind CSS (already built)
├─ init_db.py                     # DB setup
├─ init_law_firms.py              # optional seed for firms
├─ setup_database.py              # optional combined setup
├─ add_lawfirm_column.py          # migration helpers (optional)
├─ add_firm_name_column.py        # migration helpers (optional)
├─ update_firm_names.py           # migration helpers (optional)
└─ .gitignore
```

Not committed (ignored): `venv/`, `node_modules/`, `static/src/`, any `*.db`, `.env`, `__pycache__/`, `*.pyc`.

---

## Deploying Online (summary)

You can put ClientVault online using a platform like Render, Railway, or Heroku.

- Push your code to GitHub.
- On the host, create a new **Web Service** from your repo.
- **Start command:**  
  ```
  gunicorn app:app
  ```
- **Environment variables:**  
  - `SECRET_KEY` = a long random string (generate locally and copy)
  - Optional: `DATABASE_URL` if you upgrade to managed PostgreSQL.
- If you stay on SQLite, understand that many free tiers reset data on redeploy unless you attach persistent storage.

You do not need Node on the server if you commit the compiled `static/tw.css`.

---

## Troubleshooting

- **“Module not found” / import errors**  
  Make sure your virtual environment is activated and `pip install -r requirements.txt` ran successfully.

- **“Secret key not set”**  
  Set `SECRET_KEY` as shown in step 4 (or restart your terminal and set it again).

- **Styles look broken**  
  Ensure `<link rel="stylesheet" href="{{ url_for('static', filename='tw.css') }}">` exists in `templates/base.html`.  
  If you changed `static/src/tailwind.css`, rebuild `tw.css`.

- **Database changes didn’t show**  
  Restart the app after running setup scripts.

---

## Notes for Contributors

- Do not commit local databases, virtualenvs, or Node modules.
- If you change templates or styles, remember to rebuild `static/tw.css` before committing.


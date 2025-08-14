# ClientVault

ClientVault is a secure, easy-to-use platform for law firms to manage client information.  
Each firm can log in and access only its own clients.

---

## Setup Instructions

1. Create a virtual environment and install Python dependencies  
python -m venv venv  
# macOS/Linux:  
source venv/bin/activate  
# Windows (PowerShell):  
# .\venv\Scripts\Activate.ps1  

pip install -r requirements.txt

---

2. Set a Flask SECRET_KEY (needed for sessions)  
# macOS/Linux:  
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"  

# Windows PowerShell:  
# setx SECRET_KEY (python -c "import secrets; print(secrets.token_hex(32))")

---

3. Initialize the SQLite database  
Run the scripts that create your tables and seed data. Use what your project needs:  
python init_db.py  
python init_law_firms.py  
# or, if you have a consolidated script:  
# python setup_database.py

---

4. (Optional) Rebuild Tailwind if you changed the UI  
If you edit styles in static/src/tailwind.css, rebuild to static/tw.css:  
# Install node dependencies (first time only):  
# npm install  

# Development watch mode:  
# ./node_modules/.bin/tailwindcss -i ./static/src/tailwind.css -o ./static/tw.css --watch  

# Production/minified build:  
./node_modules/.bin/tailwindcss -i ./static/src/tailwind.css -o ./static/tw.css --minify

---

5. Run the app in development mode  
python app.py  
# Visit http://127.0.0.1:5000

---

## Repository Structure
ClientVault/  
├─ app.py  
├─ requirements.txt  
├─ Procfile  
├─ tailwind.config.js  
├─ package.json  
├─ package-lock.json  
├─ templates/                 # Jinja templates (base.html, home.html, etc.)  
├─ static/  
│  └─ tw.css                  # compiled Tailwind (commit this)  
├─ init_db.py                 # DB setup scripts  
├─ init_law_firms.py  
├─ setup_database.py  
├─ add_lawfirm_column.py  
├─ add_firm_name_column.py  
├─ update_firm_names.py  
└─ .gitignore

Not committed (ignored): venv/, node_modules/, static/src/, any *.db, .env

---

## Configuration
In app.py, ensure the secret key is read from the environment (with a fallback for development):  
import os  
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")

If switching to PostgreSQL, also read DATABASE_URL from the environment and connect with psycopg2-binary.

---

## Deployment (Render, Railway, or Heroku)

1. Push the project to GitHub  
Ensure the following are committed:  
app.py, templates/, static/tw.css, requirements.txt, Procfile, tailwind.config.js, package.json, package-lock.json, .gitignore, README.md

2. Create a Web Service on the hosting platform  
- Connect your GitHub repository.  
- Start command: gunicorn app:app  
- Environment variables:  
  - SECRET_KEY = a long random string  
  - (Optional) DATABASE_URL = PostgreSQL connection string

3. Database options  
- For a quick demo: keep SQLite (may reset on redeploy unless using persistent storage)  
- For production: use managed PostgreSQL. Install the driver:  
  pip install psycopg2-binary  
  Update database connection code to use DATABASE_URL

---

## Useful Commands

Rebuild Tailwind (minified for production):  
./node_modules/.bin/tailwindcss -i ./static/src/tailwind.css -o ./static/tw.css --minify  

Run locally with a production-like server:  
gunicorn app:app -b 0.0.0.0:8000

---

## License
This project is for educational and demonstration purposes. Modify and adapt it to your needs.

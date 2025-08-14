from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'something_secret'  # Required for session tracking


# -------------------- Home --------------------
@app.route('/')
def home():
    return render_template('home.html')


# -------------------- Login --------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('clientvault.db')
        c = conn.cursor()
        c.execute("SELECT id FROM law_firms WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()

        if result:
            session['law_firm_id'] = result[0]  # store law firm ID in session
            return redirect('/dashboard')
        else:
            error = "Invalid credentials. Try again."

    return render_template('login.html', error=error)

#___________________________sign up ________________
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        firm_name = request.form['firm_name']
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('clientvault.db')
        c = conn.cursor()

        # Check if username already exists
        c.execute("SELECT * FROM law_firms WHERE username=?", (username,))
        if c.fetchone():
            error = "Username already taken. Please choose a different one."
        else:
            c.execute("INSERT INTO law_firms (firm_name, username, password) VALUES (?, ?, ?)",
                      (firm_name, username, password))
            conn.commit()
            conn.close()
            return redirect('/login')

        conn.close()

    return render_template('signup.html', error=error)


# -------------------- Dashboard --------------------
@app.route('/dashboard')
def dashboard():
    if 'law_firm_id' not in session:
        return redirect('/login')

    law_firm_id = session['law_firm_id']

    conn = sqlite3.connect('clientvault.db')
    c = conn.cursor()
    c.execute("SELECT firm_name FROM law_firms WHERE id = ?", (law_firm_id,))
    firm_name = c.fetchone()[0]
    conn.close()

    return render_template('dashboard.html', firm_name=firm_name)


# -------------------- Add Client Form --------------------
@app.route('/add-client')
def add_client():
    if 'law_firm_id' not in session:
        return redirect('/login')
    return render_template('add_client.html')


# -------------------- Handle Client Submission --------------------
@app.route('/submit-client', methods=['POST'])
def submit_client():
    if 'law_firm_id' not in session:
        return redirect('/login')
    
    law_firm_id = session['law_firm_id']

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    dl_number = request.form['dl_number']
    date_of_loss = request.form['date_of_loss']

    print("New client submitted:")
    print(first_name, last_name, email, phone, dl_number, date_of_loss)

    conn = sqlite3.connect('clientvault.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO clients (first_name, last_name, email, phone, dl_number, date_of_loss, law_firm_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, email, phone, dl_number, date_of_loss, law_firm_id))

    conn.commit()
    conn.close()

    return redirect('/clients')


# -------------------- View Clients --------------------
@app.route('/clients')
def clients():
    if 'law_firm_id' not in session:
        return redirect('/login')
    
    law_firm_id = session['law_firm_id']

    conn = sqlite3.connect('clientvault.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clients WHERE law_firm_id=?", (law_firm_id,))
    all_clients = c.fetchall()
    conn.close()

    return render_template('clients.html', clients=all_clients)


# -------------------- Logout --------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# -------------------- Search clients ------------------

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'law_firm_id' not in session:
        return redirect('/login')
    law_firm_id = session['law_firm_id']

    results = []
    msg = None
    # keep form values after submit
    q = {
        'first_name': '',
        'last_name': '',
        'email': '',
        'phone': '',
        'dl_number': '',
        'date_of_loss': ''
    }

    if request.method == 'POST':
        for k in q.keys():
            q[k] = request.form.get(k, '').strip()

        if not any(q.values()):
            msg = "Enter at least one field to search."
        else:
            sql = "SELECT * FROM clients WHERE law_firm_id = ?"
            params = [law_firm_id]

            def add_like_ci(field, value):
                nonlocal sql, params
                if value:
                    sql += f" AND UPPER({field}) LIKE ?"
                    params.append(f"%{value.upper()}%")

            add_like_ci("first_name", q['first_name'])
            add_like_ci("last_name",  q['last_name'])
            add_like_ci("email",      q['email'])
            add_like_ci("phone",      q['phone'])
            add_like_ci("dl_number",  q['dl_number'])

            if q['date_of_loss']:
                sql += " AND date_of_loss = ?"
                params.append(q['date_of_loss'])

            sql += " ORDER BY last_name COLLATE NOCASE, first_name COLLATE NOCASE"

            conn = sqlite3.connect('clientvault.db')  # keep your existing DB name
            c = conn.cursor()
            c.execute(sql, params)
            results = c.fetchall()
            conn.close()

    return render_template('search.html', results=results, q=q, msg=msg)



# -------------------- Run the App --------------------
if __name__ == '__main__':
    app.run(debug=True)

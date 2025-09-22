from flask import Flask, request, redirect, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_COOKIE_PATH'] = '/sqli/'

def checkInp(inputString): #ここではじく
    ngWords = [" OR ", " AND ", " or ", " and "]
    for word in ngWords:
        if word in inputString:
            return False
    return True

@app.route('/sqli/')
def index():
    return '''
    <html>
    <head>
        <title>Login</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <div class="card p-4 shadow" style="max-width: 400px; margin: auto;">
                <h3 class="text-center mb-3">Log in</h3>
                <form method="post" action="/sqli/login">
                    <div class="mb-3">
                        <label>Username</label>
                        <input name="username" class="form-control">
                    </div>
                    <div class="mb-3">
                        <label>Password</label>
                        <input name="password" type="password" class="form-control">
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/sqli/login', methods=['POST'])
def login():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()

    if not checkInp(username) or not checkInp(password):
        return "<div class='container mt-5 alert alert-danger'><h1>Illegal characters detected ('Д')</h1></div>"
    if username == 'Freddie':
        query = f"SELECT * FROM NCTFDBUsers WHERE username = '{username}' AND password = '{password}'"
    else:
        hashed = hashlib.sha256(password.encode()).hexdigest()
        query = f"SELECT * FROM NCTFDBUsers WHERE username = '{username}' AND password = '{hashed}'"

    conn = sqlite3.connect("Northwind.db")
    cur = conn.cursor()
    try:
        cur.execute(query)
        rows = cur.fetchall()
    except Exception as e:
        return f"<div class='container mt-5'><div class='alert alert-warning'>SQL Error: {e}</div></div>"
    finally:
        conn.close()

    if len(rows) > 1:
        html = '''<div class="container mt-5"><h2>Oops... Confidential Employee Directory Exposed!</h2><table class="table table-bordered table-striped bg-white shadow"><thead><tr><th>Username</th><th>Phone</th><th>Department</th></tr></thead><tbody>'''
        for row in rows:
            html += f"<tr><td>{row[1]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
        html += '''</tbody></table><div style="margin-top: 30px; padding: 20px; background-color: #fff8dc; border: 1px solid #f0e68c; border-radius: 8px; font-family: sans-serif;"><p style="font-size: 18px; font-weight: bold; color: #d9534f;">SQLI is available (ﾟдﾟ)！</p><ul style="list-style-type: disc; margin-left: 20px; font-size: 16px; color: #333;"><li>Try to <span style="color: #5bc0de; font-weight: bold;">discover the number of the columns</span>.</li><li>Then, <span style="color: #5bc0de; font-weight: bold;">find out the table name(Hint: This app is using light weight DB)</span>.</li><li>Next, <span style="color: #5bc0de; font-weight: bold;">enumerate the column names</span>.</li><li>After that, <span style="color: #f0ad4e; font-weight: bold;">try your SQLi attack!!</span></li></ul><p style="margin-top: 20px; font-size: 18px; font-weight: bold; color: #d9534f;">You are close to the <span style="color: #f0ad4e;">Flag</span>! Can you log in as <span style="color: #5cb85c;">admin role</span>? ('Д')!</p></div>'''
        return html

    for row in rows:
        if row[1] == username and row[2] == password:
            return redirect('/sqli/soundonly')
        if row[1] == username and row[2] == hashed:
            if row[6] == 'administrator':
                session['admin_login'] = True
                return redirect('/sqli/adminonly')
            return f"<div class='container mt-5 alert alert-success'>Welcome {username}! (but you're not admin) ('Д')</div><a href='/sqli/'>Back</a>"
    return "<div class='container mt-5 alert alert-danger'><h2>Login Failed!</h2><p>Check your username and password...</p><a href='/sqli/'>Back</a></div>"

@app.route('/sqli/adminonly')
def admin():
    if not session.get('admin_login'):
        return redirect('/sqli/')
    return '''<div class="container mt-5"><div class="alert alert-success"><h2>Congratulations, Administrator!</h2><p>Flag: <strong>NCTF{U_Logg3d_iN_4S_4Dm1n}</strong></p></div><a href="/sqli/">Back</a></div>'''
#-------------------追加
@app.route('/sqli/soundonly')
def freddie():
    return '''<div class="container mt-5"><div class="alert alert-success"><h2>Login Success!</h2><p>but you are not admin! check your <strong>role</strong></p><p>Please call me</p></div><a href="/sqli/">Back</a></div>'''
#------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

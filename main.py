from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secretkey"
app.permanent_session_lifetime = timedelta(days=1)


@app.route('/dashboard', methods=["POST", "GET"])
def dashboard():
    if "username" in session:
        if "password" in session:
            username = session["username"]
            password = session["password"]
            return render_template('dashboard.html')
    else:
        return redirect(url_for("login"))


@app.route('/', methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] == 'admin' or request.form['password'] == 'password':
            if request.form.getlist('rememberme').__contains__('checked'):
                session.permanent = True
                print("Setting permanent session to 1 day(s).")
            username = request.form['username']
            password = request.form['password']
            session['username'] = username
            session['password'] = password
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid login. Please try again.'
    return render_template('login/login.html', error=error)


# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"

# session.pop("username", "password", None)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

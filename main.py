from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('index.html')


@app.route('/<name>')
def user(name):
    return f"Hello {name}!"


@app.route('/admin')
def admin():
    return redirect(url_for("user", name="Admin"))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

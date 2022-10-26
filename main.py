from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/<name>')
def content(name):
    return render_template('content.html', content=name, r=random.randint(1, 5), list=["Ethan", "Zach", "Molly"])


@app.route('/admin')
def admin():
    return redirect(url_for('user', name="Admin"))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

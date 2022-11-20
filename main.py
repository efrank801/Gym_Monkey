# Imports
from flask import Flask, render_template


# Starting Flask Application
app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/', methods=["POST", "GET"])
def login():
    render_template('login.html')


# Run
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

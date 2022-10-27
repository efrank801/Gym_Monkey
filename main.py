from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
    return render_template('login.html')


# @app.route('/login', methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         usr = request.form["nm"]
#         return redirect(url_for("user", usr=usr))
#     else:
#         return render_template('login.html')


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

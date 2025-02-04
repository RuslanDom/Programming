from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/login")
def login():
    pass

@app.route("/user/<username>")
def profile(username):
    pass

""" Построение (генерация) URL """
with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next='/'))
    print(url_for("profile", username='Buddy Man'))

# RESULT:
# /
# /login
# /login?next=/
# /user/Buddy%20Man


if __name__ == "__main":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
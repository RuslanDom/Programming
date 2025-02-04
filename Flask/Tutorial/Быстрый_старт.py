from flask import Flask

app = Flask(__name__)

@app.route("/", method=["GET"])
def start_app():
    return "Start working program"

@app.route("/hello")
def hello():
    return "Hello world!"

@app.route("/user/<username>")
def user_hello(username: str):
    return "User name is %s" % username

@app.route("/post/<post_id>")
def get_post(post_id: int):
    return "User ID %d" % post_id


@app.route('/projects/')
def projects():
    return 'The project page'
@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)


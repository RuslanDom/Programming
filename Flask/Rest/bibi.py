from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = Flask
    app.run(debug=True)
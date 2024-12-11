from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    return "This is empty page"

if __name__ == "__main__":
    app.run(debug=False)
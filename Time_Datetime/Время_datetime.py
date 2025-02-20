from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/time")
def get_time():
    return f"Московское время {datetime.now()}"


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)






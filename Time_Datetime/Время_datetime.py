from flask import Flask
import datetime as d

app = Flask(__name__)

@app.route("/time")
def get_time():
    return f"Московское время {d.datetime.now()}"


@app.route("/delta_days")
def get_delta_days():
    """
    Запрос curl http://localhost:5000/delta_days
    """
    date_1 = d.date(2025, 1, 1)
    date_2 = d.date(2025, 12, 31)
    delta_days = date_2 - date_1
    print(delta_days)
    return {"delta_days": delta_days.days}, 200


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)






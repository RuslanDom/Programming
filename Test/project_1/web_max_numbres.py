from flask import Flask

app = Flask(__name__)

@app.route("/max/<path:num>")
def max_nums(num):
    res = [int(n) for n in num.split('/')]
    return f"Максимальное число: {max(res)}"


if __name__ == "__main__":
    app.run(debug=True)


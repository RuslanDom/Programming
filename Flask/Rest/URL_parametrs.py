import os.path

from flask import Flask


app = Flask(__name__)

@app.route("/hello/<username>")
def hello(username):
    return f"Hello, {username} world"

@app.route("/check/<int:number>")
def check_numbers(number):
    if number % 2:
        result = "odd (нечётное)"
    else:
        result = "even (чётное)"
    return f"Number: {number} is <b>{result}</b>"



@app.route("/compare/<float:number_1>/<float:number_2>")
def compare(number_1: float, number_2: float):
    if number_1 < number_2:
        result = '<'
    elif number_1 > number_2:
        result = '>'
    else:
        result = '='
    return f"<h3>Compare</h3> {number_1} {result} {number_2}"


@app.route("/exists/<path:file_path>")
def exists(file_path: str):
    """
    Check if file with relative path exists in file system
    :param file_path: the relative path
    :return: http response
    """
    file_exists = os.path.exists(file_path)
    result = "exists" if file_exists else "does not exist"
    status_code = 200 if file_exists else 404

    return f"File <h4>{file_path}</h4> {result}", status_code


if __name__ == "__main__":
    app.run(debug=True)



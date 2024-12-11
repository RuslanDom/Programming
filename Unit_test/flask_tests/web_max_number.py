from flask import Flask

app = Flask(__name__)

@app.route('/max/<path:nums>')
def max_numbers(nums):
    numbers = (int(num) for num in nums.split('/'))
    return f"Максимальное число из переданных: {max(numbers)}"


if __name__ == "__main__":
    app.run(debug=True, port=5555)
from flask import Flask, request
from typing import List, Optional
from numpy import array, multiply


app = Flask(__name__)

# Ввод: http://127.0.0.1:5000/array/?el_arr1=1&el_arr1=2&el_arr1=3&el_arr2=4&el_arr2=5&el_arr2=6

@app.route("/array/", methods=["GET"])
def work_with_array():
    array_1: List[int] = request.args.getlist('el_arr1', type=int)
    array_2: List[int] = request.args.getlist('el_arr2', type=int)

    summa_arrays = array(array_1) + array(array_2)
    multiply_arrays = multiply(array_1, array_2)

    return (
        f"Сумма массивов {array_1} и {array_2} равна: {summa_arrays} \n"
        f"Произведение массивов {array_1} и {array_2} равно: {multiply_arrays}"
    )

# Результат:
# Сумма массивов [1, 2, 3] и [4, 5, 6] равна: [5 7 9] Произведение массивов [1, 2, 3] и [4, 5, 6] равно: [4 10 18]

# Ввод: http://127.0.0.1:5000/near_value/?num=22
@app.route('/near_value/', methods=['GET'])
def near_num():
    a = [14, 42, 31, 26, 62, 55]
    s_a = sorted(a)
    print(s_a)
    x: Optional[int] = request.args.get('num', type=int, default=0)
    res = None
    for i in s_a:
        difference = abs(i - x)
        if res is None:
            res = i
        else:
            if difference < abs(res - x):
                res = i

    return f"В массиве {a} самый близкий по значению элемент к числу {x} = {res}"

# Результат: В массиве [14, 42, 31, 26, 62, 55] самый близкий по значению элемент к числу 22 = 26

if __name__ =="__main__":
    app.run(debug=True)
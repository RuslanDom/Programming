import json
from urllib.parse import unquote_plus

from flask import Flask, request


app = Flask(__name__)

# get request
@app.route('/sum_get/', methods=["GET"])
def sum_get():
    array1 = request.args.getlist("array1", type=int)
    array2 = request.args.getlist("array2", type=int)

    result = ','.join(str(a1 + a2) for (a1, a2) in zip(array1, array2))

    return f"Array of sums is [{result}]"
# Через CURL этот запрос
# ruslan@PC:~$ curl "http://localhost:5000/sum_get/?array1=1&array1=2&array2=2&array2=2"





# POSTMAN form-data
@app.route('/sum', methods=["POST"])
def _sum():
    array1 = request.form.getlist("array1", type=int)
    array2 = request.form.getlist("array2", type=int)

    result = ','.join(str(a1 + a2) for (a1, a2) in zip(array1, array2))

    return f"Array of sums is [{result}]"


# POSTMAN x-www-form-urlencoded
@app.route('/sum2', methods=["POST"])
def _sum2():
    form_data = request.get_data(as_text=True)
    decode_data = unquote_plus(form_data)

    arrays = {}

    print(f'Закодированная строка: {form_data}')  # Закодированная строка: array1=1%2C2%2C3&array2=3%2C2%2C1
    print(f"Раскодированная: {decode_data}")  # Раскодированная: array1=1,2,3&array2=3,2,1

    for each_arr in decode_data.split("&"):  # array1=1,2,3&array2=3,2,1    делим по &
        k, v = each_arr.split('=')  # array1=1,2,3 и array2=3,2,1           делим по = 

        arrays[k] = [int(num) for num in v.split(',')]  # arrays["array1"] равный 1,2,3 которые делим по ,

    result_str = ",".join(str(a1 + a2) for a1, a2 in zip(arrays["array1"], arrays["array2"]))

    return f'Сумма {arrays["array1"]} и {arrays["array2"]} равна [{result_str}]'



# POSTMAN row
@app.route('/sum3', methods=["POST"])
def _sum3_json():
    form_data = request.get_data(as_text=True)

    data_python = json.loads(form_data)  # преобразуем строку JSON 'form_data' в объект Python

    result_str = ",".join(str(a1 + a2) for a1, a2 in zip(data_python["array1"], data_python["array2"]))
    return f'Сумма {data_python["array1"]} и {data_python["array2"]} равна [{result_str}]'

# Через CURL
# ruslan@PC:~$ curl -H "json" -d'{"array1":[1,1,1],"array2":[2,3,4]}' http://localhost:5000/sum3


if __name__ == "__main__":
    app.run(debug=True)

























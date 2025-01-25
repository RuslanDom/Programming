autor = 'selfedu'
link_video = "https://www.youtube.com/watch?v=6jxveKOdyNg&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=1"

# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# @app.route("/index")
# def get_index():
#     return "<h1>Index</h1>"


# if __name__ == "__main__":
#     app.config["WTF_CSRF_ENABLED"] = False
#     app.run(debug=True, port=5050)

"-------------------------------------------------------------------------------------------------------------"
"Использование шаблонов страниц"
link_video = "https://www.youtube.com/watch?v=TSsEMFZVr5E&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=2"

from flask import Flask, render_template

app = Flask(__name__)

# Шаблоны страниц берём из подкаталога templates

# Меню для главной страницы
my_meny = ["Установка", "Первое приложение", "Обратная связь"]


@app.route("/")
def get_index():
    return render_template('index.html', 
                           title="Главная страница про Flask",
                           meny=my_meny
                           )  # Параметрами передаём инфу на html страницу


@app.route("/about")
def get_about():
    return render_template('about.html',
                           title='Страница о продукте',
                           meny=my_meny
                           ) 


@app.route("/win_doors")
def win_doors_index():
    return render_template("win_doors_index.html")


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
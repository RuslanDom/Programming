from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# Контекст приложения g, current_app
# g - сохраняет пользовательскую инф. нужную для обработки запросов (сохранить текущее соединение с БД, а после его закрыть)

# Контекст запроса request, session
# request - содержит данные связанные с текущим запросом (работает в пределах одного потока)
# session - словарь в котором можно сохранять данные в переделах сессии (связанна с одним источником запроса, т.е. пользователем)

meny = [
    {"name": "Установка", "url": "install-flask"},
    {"name": "Приложения", "url": "new-app"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route("/")
def index():
    # url_for() - функция позволяет получить url адрес используя название функции которая выполняется по этому адресу
    print(url_for("index"))
    return render_template('index.html', meny=meny)


@app.route("/about")
def about():
    print(url_for("about"))
    return render_template("about.html", meny=meny, title="О сайте")


@app.route("/profile/<username>")
def profile(username):
    return "<h1>Пользователь: %s</h1>" % username


@app.route("/set_age/<int:age>/<path:other>")  # path - можно использовать все символы URL и знак /
def set_age(age, other):
    return "<h1>Возраст: %s Другое: %s</h1>" % (age, other)


# Работа с form
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
        print(request.form["username"])
        print(request.form["email"])
        print(request.form["message"])
    return render_template("contact.html", title="Контакты", meny=meny)


# Тестовый контекст запроса
# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("profile", username="Host page"))
#     print(url_for("set_age", age=35, other="From Russia"))

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

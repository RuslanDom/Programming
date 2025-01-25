# Мгновенные сообщения, обработка ответов сервера

# flash(message="", category='message')
# get_flashed_messages(with_categories=False, category_filter=[])

# message - текст сообщения
# category - категория сообщения
# with_categories - разрешает использование категорий при извлечении сообщений
# category_filter - список разрешенных категорий при выборке сообщений


from flask import Flask, render_template, url_for, request, flash, get_flashed_messages, session, redirect, abort
import os

app = Flask(__name__)

# Секретный ключ для session
app.config["SECRET_KEY"] = os.urandom(10).hex()
print(app.config["SECRET_KEY"])

meny = [
    {"name": "Главная", "url": "index"},
    {"name": "Авторизация", "url": "login"},
    {"name": "Установка", "url": "install-flask"},
    {"name": "Приложения", "url": "new-app"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route("/")
@app.route("/index")
def index():
    print(url_for("index"))
    return render_template('index.html', meny=meny)


@app.route("/about")
def about():
    print(url_for("about"))
    return render_template("about.html", meny=meny, title="О сайте")


# Работа с form
@app.route("/contact", methods=["POST", "GET"])
def contact():

    if request.method == "POST":
        if len(request.form["username"]) > 3:
            flash("Сообщение отправлено успешно", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template("contact.html", title="Контакты", meny=meny)


# L7 Декоратор errorhandler, функции redirect и abort

# Авторизация обработка страницы
@app.route("/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for('profile', username=session["userLogged"]))
    elif request.method == "POST" and request.form["username"] == "ruslan" and request.form["password"] == '123':
        session["userLogged"] = request.form["username"]
        return redirect(url_for('profile', username=session["userLogged"]))
    return render_template("login.html", title="Авторизация", meny=meny)


@app.route("/profile/<username>")
def profile(username):
    # Ошибка 401 и abort(прерывание) условие доступа только для конкретного пользователя
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return render_template("profile.html", title=username, meny=meny)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", meny=meny), 404

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

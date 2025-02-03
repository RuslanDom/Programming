from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# создать приложение
app = Flask(__name__)
# настроить базу данных SQLite относительно папки с экземплярами приложения
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_db.db"
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Users %r>" % self.id

# ИНИЦИАЛИЗАЦИЯ БД
# with app.app_context():
#     db.create_all()


@app.route('/', methods=["POST", "GET"])
def create_users():
    if request.method == "POST":
        username = request.form["username"]
        text = request.form["text"]

        new_user = Users(username=username, text=text)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/")
        except:
            return "Произошла ошибка"
    else:
        return render_template("create_users.html")


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)








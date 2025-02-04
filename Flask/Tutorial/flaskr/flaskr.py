# все импорты
import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

# конфигурация
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# создаём наше маленькое приложение
app = Flask(__name__)
# Загружаем конфиг по умолчанию и переопределяем в конфигурации часть
# значений через переменную окружения
app.config.from_object(__name__)

# config работает подобно словарю, поэтому мы можем обновлять его с помощью новых значений
app.config.update(
    dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        DEBUG=True,
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    )
)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Соединяет с указанной базой данных."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Создаёт соединение или возвращает уже имеющееся через app
def get_db():
    """Если ещё нет соединения с базой данных, открыть новое - для
    текущего контекста приложения
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Закрывает соединение
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# Инициализатор БД
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()

# Функция представления
"""Это представление показывает все записи, хранящиеся в базе данных. Оно соответствует
 главной странице вашего приложения, и выбирает все заголовки и тексты из
базы данных. Запись с наибольшим id (последняя по времени) будет наверху."""
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('''SELECT title, text FROM entries ORDER BY id desc''')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

# Добавление новой записи
"""Это представление позволяет пользователю, если он осуществил вход, добавлять
новые записи. Оно реагирует только на запросы типа POST, а фактическая форма
отображается на странице show_entries"""
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('INSERT INTO entries (title, text) VALUES (?, ?)',
    [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

# Инициализатор БД (запускается единожды)
# init_db()

if __name__ == "__main__":
    app.run(debug=True)



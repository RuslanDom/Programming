from flask import Flask, session, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
				<form action="" method="post">
					<p><input type=text name=username>
					<p><input type=submit value=Login>
				</form>
			'''


@app.route('/logout')
def logout():
	# удалить из сессии имя пользователя, если оно там есть
	session.pop('username', None)
	return redirect(url_for('index'))

# Генерация секретного ключа
import os
msk = os.urandom(24).hex()

# set the secret key. keep this really secret:
app.secret_key = msk



if __name__ == "__main__":
	app.config['WTF_CSRF_ENABLED'] = False
	app.run(debug=True)


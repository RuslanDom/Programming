from flask import Flask
from models import get_all_books


app = Flask(__name__)

@app.route('/books')
def all_books():
    ...



if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
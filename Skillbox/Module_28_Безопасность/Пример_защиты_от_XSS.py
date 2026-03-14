from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    # Данные от пользователя (потенциально опасные)
    user_input = "<script>alert('XSS')</script>"

    # Шаблон в виде строки
    template = "<h1>Привет, {{ name }}!</h1>"

    # Автоматическое экранирование произойдет здесь
    return render_template_string(template, name=user_input)

# Результат в браузере: <h1>Привет, &lt;script&gt;alert('XSS')&lt;/script&gt;!</h

if __name__ == '__main__':
    app.run(debug=True)
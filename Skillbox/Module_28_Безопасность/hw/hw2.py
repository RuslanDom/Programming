"""
Давайте воспользуемся политикой безопасности контента и воспроизведем поведение первого уровня игры,
добавив в ответ веб-сервера нужные хедеры, которые запретят выполнение встроенных скриптов
(тех, которые мы помещали внутри хедера и которые запускались уже после загрузки всей страницы).
Для верстки можно воспользоваться следующим шаблоном:

"""

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  {user_input}
</body>
</html>
"""

page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <script src="/static/game-frame.js"></script>
    <link rel="stylesheet" href="/static/game-frame-styles.css" />
  </head>

  <body id="level1">
    <img src="/static/logos/level1.png">
      <div>
"""

page_footer = """
    </div>
  </body>
</html>
"""

main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""

# import webapp2
#
# class MainPage(webapp2.RequestHandler):
#
#     def render_string(self, s):
#         self.response.out.write(s)
#
#     def get(self):
#         # Disable the reflected XSS filter for demonstration purposes
#         self.response.headers.add_header("X-XSS-Protection", "0")
#
#         if not self.request.get('query'):
#             # Show src search page
#             self.render_string(page_header + main_page_markup + page_footer)
#         else:
#             query = self.request.get('query', '[empty]')
#
#             # Our search engine broke, we found no results :-(
#             message = "Sorry, no results were found for <b>" + query + "</b>."
#             message += " <a href='?'>Try again</a>."
#
#             # Display the results page
#             self.render_string(page_header + message + page_footer)
#
#         return
#
#
# application = webapp2.WSGIApplication([('/', MainPage), ], debug=True)

from flask import Flask, render_template_string, request
from markupsafe import escape
from jinja2 import Template

XSS_ATTACK = '<script>alert("Lose!")</script>'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if not request.args.get('query'):
        # Show src search page
        return render_template_string(page_header + main_page_markup + page_footer)
    else:
        query = request.args.get('query')

        # Our search engine broke, we found no results :-(
        message = "Sorry, no results were found for <b>" + "{{ user_query }}" + "</b>."
        message += " <a href='?'>Try again</a>."

        # Display the results page

        return render_template_string(page_header + message + page_footer, user_query=query)



if __name__ == '__main__':
    app.run(debug=True)


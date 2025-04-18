import os

from flask import Flask, render_template, send_from_directory

root_dir = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(root_dir, "templates")
static_directory = os.path.join(root_dir, 'static')
# js_directory = os.path.join(static_directory, "js")
# css_directory = os.path.join(static_directory, "css")
# images_directory = os.path.join(static_directory, "images")

app = Flask(__name__, template_folder=template_folder)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory(static_directory, path)

# @app.route("/js/<path:path>")
# def send_js(path):
#     return send_from_directory(js_directory, path)
#
#
# @app.route("/css/<path:path>")
# def send_css(path):
#     return send_from_directory(css_directory, path)
#
#
# @app.route("/images/<path:path>")
# def send_images(path):
#     return send_from_directory(images_directory, path)


if __name__ == "__main__":
    app.run()

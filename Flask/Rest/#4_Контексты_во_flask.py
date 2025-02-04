from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def request_data():
    return f"Hello,! Your IP is {request.remote_addr} and you are using {request.user_agent}"





if __name__ == "__main__":
    app.run(debug=True)
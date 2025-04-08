from flask_jsonrpc import JSONRPC
from flask  import Flask


app = Flask(__name__)
jsonrpc = JSONRPC(app=app,
                  service_url="/api",
                  enable_web_browsable_api=True
                  )

@jsonrpc.method("App.index")
def index():
    return {"message": "Hello World"}

if __name__ == '__main__':
    app.run(debug=True)




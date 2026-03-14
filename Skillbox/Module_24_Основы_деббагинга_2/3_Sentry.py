import sentry_sdk
import logging
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask, request

sentry_sdk.init(
    dsn="https://8c3080add08d2b08e4e9d280d28cd407@o4510846692884480.ingest.de.sentry.io/4510846705795152",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)


app = Flask(__name__)

@app.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0


@app.route("/etest_type")
def etest_type():
    user_id = float(request.args.get("user_id"))


@app.route("/etest_logging")
def etest_logging():
    logging.error("Error to log")



if __name__ == "__main__":
    app.run()













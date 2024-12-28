import logging
import flask

from http_utils import get_ip_address
from subprocess_utils import get_kernel_version


root_logger = logging.getLogger()
root_logger.setLevel('WARNING')  # Корневой логгер на WARNING

logger = logging.getLogger('main')
logger.setLevel('DEBUG')  # main на DEBUG

utils = logging.getLogger('logger_utils')
utils.setLevel("DEBUG")  # logger_utils на DEBUG

logging.basicConfig(
                    format='%(name)s : %(levelname)s - %(message)s'
                    )

app = flask.Flask(__name__)


@app.route('/get_system_info')
def get_system_info():
    logger.info('Start working')
    ip = get_ip_address()
    kernel = get_kernel_version()
    return "<p>{}</p><p>{}</p>".format(ip, kernel)


if __name__ == "__main__":
    app.run(debug=True)
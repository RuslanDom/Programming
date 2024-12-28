import logging
import time
import requests

logger = logging.getLogger('logger_utils.http_utils')  # sublogger logger_utils.http_utils
logger.setLevel('INFO')
GET_IP_URL = 'https://api.ipify.org?format=json'


def get_ip_address() -> str:
    logger.info("Start getting ip")
    start = time.time()
    try:
        ip = requests.get(GET_IP_URL).json()['ip']
    except Exception as e:
        logger.exception(e)
        raise e
    logger.info('Done requesting ip in {:.4f} sec'.format(time.time()-start))
    logger.info('IP address: {}'.format(ip))
    return ip

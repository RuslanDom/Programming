import logging
import time
import requests

logger = logging.getLogger('http_utils')

GET_IP_URL = 'https://api.ipify.org?format=json'


def get_ip_address() -> str:
    logger.debug("Start get ip")
    start = time.time()
    try:
        ip = requests.get(GET_IP_URL).json()['ip']
    except Exception as e:
        logger.exception(e)
        raise e
    logger.debug('Done requesting ip in {:.4f} sec'.format(time.time()-start))
    logger.info('IP address: {}'.format(ip))
    return ip

import logging
import subprocess
import shlex

KERNEL_VERSION = None

logger = logging.getLogger('logger_utils.subprocess_utils')  # sublogger logger_utils.subprocess_utils
logger.setLevel('DEBUG')  # subprocess_utils на DEBUG

def get_kernel_version() -> str:
    logger.info('Start getting kernel')
    command = shlex.split('uname -a')
    global KERNEL_VERSION
    if KERNEL_VERSION is None:
        logger.debug("Kernel version is not defined. Start subprocess call")
        try:
            out = subprocess.run(command, capture_output=True, encoding='utf-8')
        except Exception as e:
            logger.exception(e)
            raise e
        KERNEL_VERSION = out.stdout.strip()
        logger.debug('Kernel version: {}'.format(KERNEL_VERSION))
    logger.info('Return kernel version')
    return KERNEL_VERSION


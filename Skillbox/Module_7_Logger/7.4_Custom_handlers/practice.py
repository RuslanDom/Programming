import logging
import logging.config
from practice_config import dict_config

logging.config.dictConfig(dict_config)
logger = logging.getLogger('logger')
logger.setLevel('DEBUG')


def main():
    logger.info("Start")
    logger.debug("Beginning...")
    logger.debug("Making...")
    logger.debug("Disable making")
    logger.info("Stop")


if __name__ == "__main__":
    main()

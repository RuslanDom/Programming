import logging

root_log = logging.getLogger()

logger = logging.getLogger('Main_logger')
logger.setLevel('INFO')
logger.propagate = False
custom_logger = logging.StreamHandler()
logger.addHandler(custom_logger)
format_logs = logging.Formatter('%(name)s : %(asctime)s : %(message)s')
custom_logger.setFormatter(format_logs)
file_logger = logging.FileHandler('My_logs.log', 'a')
file_logger.setFormatter(format_logs)
logger.addHandler(file_logger)


sub_logger = logging.getLogger('Main_logger.Sub_logger')
sub_logger.setLevel('DEBUG')
sub_logger.propagate = False
custom_sub_logger = logging.StreamHandler()
sub_logger.addHandler(custom_sub_logger)
format_sub_logs = logging.Formatter('%(name)s | %(levelname)s | %(asctime)s | %(message)s')
custom_sub_logger.setFormatter(format_sub_logs)
file_sub_logger = logging.FileHandler('My_logs.log' , 'a')
file_sub_logger.setFormatter(format_sub_logs)
sub_logger.addHandler(file_sub_logger)


def main():
    print(root_log)
    print(logger)
    print(sub_logger)
    logger.info('Start working program')
    sub_logger.debug('Working...')
    sub_logger.debug('Finish')
    sub_logger.info('Getting result')
    logger.info('End working program')


if __name__ == "__main__":
    main()

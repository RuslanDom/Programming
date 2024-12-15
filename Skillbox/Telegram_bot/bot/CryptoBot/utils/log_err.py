import functools
import logging


def log_error(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as err:
            logging.exception(err)
    return wrapped

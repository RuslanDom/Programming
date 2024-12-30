import logging
import sys


class CustomStreamHandler(logging.Handler):
    def __init__(self, stream: sys.stderr):
        super().__init__()
        self.stream = stream

    def emit(self, record: logging.LogRecord):
        message = self.format(record)
        sys.stderr = message
        print(sys.stderr)
        sys.stderr = self.stream


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(name)s - %(asctime)s - %(levelname)s - %(message)s"
        }
    },
    "handlers":{
        "console": {
            "()": CustomStreamHandler,
            "level": "DEBUG",
            "formatter": "base",
            "stream": sys.stderr
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "custompracticelog.lod",
            "mode": "a"
        }
    },
    "loggers": {
        "logger": {
            "level": "DEBUG",
            "handlers": ["file", "console"]
        }
    }
}


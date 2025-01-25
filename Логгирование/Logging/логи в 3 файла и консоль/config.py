import logging.handlers
import sys


class ErrorFileHandler(logging.Filter):
    def filter(self, record: logging.LogRecord):
        if record.levelno == 40:
            return True


class InfoFileHandler(logging.Filter):
    def filter(self, record: logging.LogRecord):
        if record.levelno == 20:
            return True


class DebugFileHandler(logging.Filter):
    def filter(self, record: logging.LogRecord):
        if record.levelno == 10:
            return True


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "general": {
            "format": "%(name)s - %(levelname)s - %(lineno)s - %(asctime)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": logging.StreamHandler,
            "level": "DEBUG",
            "formatter": "general",
            'stream': sys.stdout
        },
        "file_debug": {
            "class": logging.FileHandler,
            "level": "DEBUG",
            "filename": "log_debug.log",
            "formatter": "general",
            "encoding": "utf-8",
            "filters": ["debug_filter"]
        },
        "file_info": {
            "class": logging.FileHandler,
            "level": "DEBUG",
            "filename": "log_info.log",
            "formatter": "general",
            "encoding": "utf-8",
            "filters": ["info_filter"]
        },
        "file_error": {
            "class": logging.FileHandler,
            "level": "DEBUG",
            "filename": "log_error.log",
            "formatter": "general",
            "encoding": "utf-8",
            "filters": ["error_filter"]
        }
    },
    "filters": {
        "debug_filter": {
            "()": DebugFileHandler
        },
        "info_filter": {
            "()": InfoFileHandler
        },
        "error_filter": {
            "()": ErrorFileHandler
        }
    },
    "loggers": {
        "main": {
            "level": "DEBUG",
            "handlers": ["console", "file_error", "file_info", "file_debug"]
        }
    }
}

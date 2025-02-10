import sys
import logging
from logging import handlers

dict_config = {
        "version": 1,
        "disable exiting loggers": False,
        "formatters": {
                    "base": {
                        "format": "%(name)s | %(asctime)s | %(levelname)s | %(message)s"
                    }
        },
        "handlers": {
            "console": {
                "class": logging.StreamHandler,
                "level": "DEBUG",
                "formatter": "base",
                "stream": sys.stdout
            },
            "file": {
                "class": handlers.TimedRotatingFileHandler,
                "when": "H",
                "interval": 2,
                "level": "WARNING",
                "formatter": "base",
                "filename": "logs/logs_warning.log",
                "backupCount": 1,
            }
        },
        "loggers" : {
            "main":{
                "level": "DEBUG",
                "handlers": ["console",  "file"]
            }
        },
        "filters": {}
}
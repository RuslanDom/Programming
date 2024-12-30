import logging, sys, logging.handlers

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(name)s | %(asctime)s | %(levelname)s | %(message)s |"
        }
    },
    "handlers": {
        "screen": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": sys.stdout
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",  # Удаляет устаревшие логи
            "when": "midnight",  # Каждую полночь бэкап логов
            "backupCount": 5,  # Не более 5 дней логов
            "level": "ERROR",
            "formatter": "simple",
            "filename": "workers_logs.log"
        }
    },
    "loggers": {
        "main": {
            "level": "DEBUG",
            "handlers": ["screen"]
        }
    }
}


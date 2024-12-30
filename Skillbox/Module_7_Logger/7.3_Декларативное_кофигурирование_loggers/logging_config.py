
dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(name)s | %(levelname)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "logfile.log",
            "mode": "a"
        }
    },
    "loggers": {
        "logger": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
            # "propagate": False
        }
    },

    # "filters": {},
    # "root": {} == "": {}
}

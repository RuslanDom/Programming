import logging


class CustomFileHandler(logging.Handler):
    def __init__(self, filename, mode='a'):
        super().__init__()  # Для того чтобы наш объект получил все необходимые атрибуты от родительского класса
        self.filename = filename
        self.mode = mode

    # Метод для подготовки и отправке сообщений
    def emit(self, record: logging.LogRecord) -> None:
        # record - эта та ЛОГ-запись которую мы прописали logger.debug() or logger.info()
        message = self.format(record)  # Применяем к ЛОГ-записи форматер
        with open(self.filename, self.mode) as f:
            f.write(message + '\n')  # Записываем в файл


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
            "()": CustomFileHandler,
            "level": "DEBUG",
            "formatter": "base",
            "filename": "customlogfile.log",
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
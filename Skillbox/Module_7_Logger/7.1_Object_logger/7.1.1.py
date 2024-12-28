import logging

root_logger = logging.getLogger()  # Создание корневого логгера (создаётся автоматически)
root_logger.setLevel('DEBUG')  # Установка уровня логгера (по умолчанию WARNING)
module_logger = logging.getLogger('module_logger')  # Создание именованного логгера (идёт ниже по иерархии root логгера)
submodule_logger = logging.getLogger('module_logger.submodule_logger')  # Создание sublogger-ов через <name>.<subname>
submodule_logger.setLevel('INFO')

def main():
    print(module_logger.parent)
    print(module_logger) or print(submodule_logger.parent)  # Одно и тоже
    print(submodule_logger)


if __name__ == "__main__":
    main()

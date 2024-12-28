import logging

# ROOT
root_logger = logging.getLogger()
root_logger.setLevel('INFO')

module_logger = logging.getLogger('module_logger')

submodule_logger = logging.getLogger('module_logger.submodule_logger')
submodule_logger.setLevel('DEBUG')  # Установка уровня DEBUG

# propagation - Распространение
submodule_logger.propagate = True
# submodule_logger.propagate = False  # логги не будут сливаться в root logger


# logging.basicConfig()  # Избавляемся от basicConfig()
custom_handler: """изготовленный обработчик"""  = logging.StreamHandler()  # Создаём StreamHandler
module_logger.addHandler(custom_handler)  # Добавляем обработчик в module_logger

formatter = logging.Formatter(fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s")  # Вид(формат) логов
custom_handler.setFormatter(formatter)  # Добавляем формат нашему обработчику

file_handler = logging.FileHandler('file_log', mode='a')  # Куда и как записывать логи
file_handler.setFormatter(formatter)  # Формат для записи логов
module_logger.addHandler(file_handler)  # Какой логгер будет писаться в файл

def main():
    print(f"Root logger: {root_logger.handlers}")
    print(f"Module logger: {module_logger.handlers}")
    print(f"Submodule logger: {submodule_logger.handlers}")

    submodule_logger.debug('Hello from Debug`s level')


if __name__ == "__main__":
    main()

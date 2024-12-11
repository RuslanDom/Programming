import signal

def raise_timeout(signum, frame):
    raise TimeoutError  # Генерируем исключение TimeoutError

signal.signal(signal.SIGALRM, raise_timeout)  # Назначаем обработчик

def my_func():
    ...
    # Ваша функция

signal.alarm(5)  # Устанавливаем ограничение по времени в 5 секунд для my_func!
try:
    my_func()
finally:
    signal.alarm(0)  # Отменяем сигнал.




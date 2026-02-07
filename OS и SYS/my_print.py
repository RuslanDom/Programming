import sys


def my_print_deep_seek(*args, **kwargs):
    """
    Аналог функции print() с использованием sys.stdout

    Args:
        *args: объекты для вывода
        sep (str): разделитель (по умолчанию ' ')
        end (str): окончание строки (по умолчанию '\n')
        file: файловый объект (по умолчанию sys.stdout)
        flush (bool): сброс буфера (по умолчанию False)
    """
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    flush = kwargs.get('flush', False)

    # Преобразуем все аргументы в строки и объединяем с разделителем
    output = sep.join(str(arg) for arg in args) + end

    # Записываем в файл
    file.write(output)

    # При необходимости сбрасываем буфер
    if flush:
        file.flush()





def my_print(text:str='', file=sys.stdout, sep:str='', end:str='\n', flush:bool=False):
    output = sep.join(str(letter) for letter in text) + end
    if flush:
        file.flush()
    sys.stdout.write(output)


text = "Hi, Buddy!"
my_print("Hello world!")
my_print(text, sep='_')
















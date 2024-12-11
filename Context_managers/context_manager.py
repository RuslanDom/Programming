
class MyContextManager:
    def __init__(self, path: str, mode: str) -> None:
        self.name = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_type, exc_val)
        self.file.close()
        return True



"""Для создания фабричной функции можно использовать contextlib.contextmanager"""
import contextlib

@contextlib.contextmanager
def my_context_manager(path: str, mode: str):
    try:
        _file = open(path, mode)
        yield _file
    except:
        print(f"Error")
    finally:
        _file.close()


if __name__ == "__main__":
    with MyContextManager('../Skillbox/Module_5_Основы_Linux/testfile.txt', 'w') as f:
        f.write('Hello')
    with my_context_manager('../Skillbox/Module_5_Основы_Linux/testfile.txt', 'w') as f:
        f.write('My dog\n')
        f.write('It`s name Jerry')

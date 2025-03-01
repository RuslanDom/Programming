import sys
"""
    # 1. сохраняем старый поток вывода
old_stdout = sys.stdout
    # 2. перенаправляем поток вывода в файл output.txt
new_stdout = open('output.txt', 'w')
sys.stdout = new_stdout
    # 3. теперь print будет выводить в файл
print('hello output.txt')
    # 4. закрываем файл и возвращаем старый поток вывода
new_stdout.close()
sys.stdout = old_stdout  # or sys.stdout = sys.__stdout__
"""

from types import TracebackType
from typing import Type, Literal, IO
import sys
import traceback


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        if self.stdout:
            sys.stdout = self.stdout
        if self.stderr:
            sys.stderr = self.stderr

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if self.stdout:
            self.stdout.close()
            sys.stdout = self.old_stdout
        if self.stderr:
            # print(exc_type, exc_val, exc_tb, file=self.stderr)  # Или так
            sys.stderr.write(traceback.format_exc())
            self.stderr.close()
            sys.stderr = self.old_stderr
        return True



from io import StringIO

def some_func():
    pass

# сохраняем ссылку, чтобы потом
# снова отобразить вывод в консоли.
tmp_stdout = sys.stdout

# В переменной `result` будет храниться все,
# что отправляется на стандартный вывод
result = StringIO()
sys.stdout = result

# Здесь все, что отправляется на стандартный вывод,
# будет сохранено в переменную `result`.
some_func()

# Снова перенаправляем вывод `sys.stdout` на консоль
sys.stdout = tmp_stdout

# Получаем стандартный вывод как строку!
result_string = result.getvalue()

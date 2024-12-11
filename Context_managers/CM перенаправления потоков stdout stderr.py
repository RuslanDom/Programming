from types import TracebackType
from typing import Type, Literal, IO
import sys



class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr
    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        print(exc_type, exc_val, exc_tb, file=self.stderr)
        self.stdout.close()
        self.stderr.close()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        return


print('Hello stdout')
stdout_file = open('stdout.txt', 'w')
stderr_file = open('stderr.txt', 'w')

with Redirect(stdout=stdout_file, stderr=stderr_file):
    print('Hello stdout.txt')
    raise Exception('Hello stderr.txt')

print('Hello stdout again')
raise Exception('Hello stderr')

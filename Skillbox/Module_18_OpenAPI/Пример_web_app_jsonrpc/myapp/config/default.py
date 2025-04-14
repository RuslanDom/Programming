import os
import sys
import pwgen

# Конфигурация
DEBUG = True
SQLDEBUG = False

SESSION_COOKIE_NAME = 'myapp'
SESSION_TYPE = 'filesystem'

TITLE = 'myapp'

# Генерируем пути до корня приложения и БД
DIR_BASE = "\\".join(os.path.dirname(os.path.abspath(__file__)).split("\\")[:-1])
DIR_DATA = DIR_BASE + "\\data"

# Генерируем secret key
# pwgen.pwgen(pw_length=12)
SECRET_KEY = "0aqetWNPVmTo"

# Логгирование
LOG_FILE = DIR_BASE + "\\myapp.log"
LONG_LOG_FORMAT = "%(asctime)s - [%(name)s.%(levelname)s] [%(threadName)s, %(module)s.%(funcName)s@%(lineno)d] - %(message)s"
LOG_FILE_SIZE = 128 #  Размер файла лога
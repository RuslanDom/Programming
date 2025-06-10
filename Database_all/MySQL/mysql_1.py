import pymysql
from pymysql.cursors import DictCursor

user = 'ruslan'
host = '127.0.0.1'
password = '1801_Butcher'
db_name = 'test_db'

try:
    conn = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        passwd=password,
        database=db_name,
        cursorclass=DictCursor
    )
    print("Successfully connected to MySQL")

except Exception as e:
    print("Failed to connect to MySQL")
    print(e)

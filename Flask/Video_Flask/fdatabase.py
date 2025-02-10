import sqlite3
from string import Template


class FDatabase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Error read of database")
        return []

    def addPost(self, _theme, _news):
        sql = Template("""INSERT INTO posts (theme, news) VALUES ('$theme', '$news')""").substitute(theme=_theme, news=_news)
        try:
            self.__cur.execute(sql)
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Error", e)



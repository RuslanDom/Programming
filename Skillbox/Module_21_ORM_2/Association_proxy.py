from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.ext.associationproxy import association_proxy


endine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=endine)
session = Session()

# integration table для использования двойного primary_key
user_keyword_table = Table(
    "user_keyword",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("keyword_id", Integer, ForeignKey("keyword.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))

    kw = relationship("Keyword", secondary=lambda : user_keyword_table)

    # proxy the 'keyword' attribute from the 'kw' relationship
    keywords = association_proxy('kw', 'keyword')

    # То же самое с использованием creator
    # keywords = association_proxy(
    #     "kw", "keyword", creator=lambda kw: Keyword(keyword=kw)
    # )

    def init(self, name):
        self.name = name


class Keyword(Base):
    __tablename__ = "keyword"
    id = Column(Integer, primary_key=True)
    keyword = Column(String(30))

    def init(self, keyword):
        self.keyword = keyword



if __name__ == '__main__':
    Base.metadata.create_all(endine)
    user = User("jek")
    user.keywords.append("cheese-inspector")
# >>> user.keywords
# ['cheese-inspector']

    user.keywords.append("snack ninja")
# >>> user.kw
# [<__main__.Keyword object at 0x12cdd30>, <__main__.Keyword object at 0x12cde30>]
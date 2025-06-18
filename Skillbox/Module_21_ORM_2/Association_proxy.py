from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    kw = relationship("Keyword", secondary=lambda: user_keyword_table)

    keywords = association_proxy("kw", "keyword")

    def __init__(self, name):
        self.name = name


class Keyword(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True)
    keyword = Column("keyword", String(64))

    def __init__(self, keyword):
        self.keyword = keyword


user_keyword_table = Table(
    "user_keyword",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("keyword_id", Integer, ForeignKey("keywords.id"), primary_key=True),
)

if __name__ == "__main__":
    user = User("JIEK")
    user.kw.append(Keyword("Orange"))
    user.keywords.append("Purple")
    print(user.keywords)
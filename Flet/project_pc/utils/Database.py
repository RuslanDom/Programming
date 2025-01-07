from sqlalchemy import create_engine, Table, MetaData, select, insert, and_
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
import os


class Database:
    def __init__(self):
        load_dotenv()
        self.db_host = os.getenv('DB_HOST')
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_pass = os.getenv('DB_PASS')
        # Строка подключения
        self.connect = f"postgresql+psycopg2://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}"
        self.engine = create_engine(self.connect)
        self.metadata = MetaData()
        self.Base = declarative_base()

        self.users = Table("users", self.metadata, autoload_with=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def check_email(self, email):
        result = self.session.execute(select(self.users).where(self.users.c.email == email))
        return result.fetchone()

    def check_login(self, login):
        result = self.session.execute(select(self.users).where(self.users.c.login == login))
        return result.fetchone()

    def insert_user(self, login, email, userpass):
        self.session.execute(insert(self.users).values(login=login, email=email, userpass=userpass))
        self.session.commit()

    def authorization_user(self, login, userpass):
        result = self.session.execute(select(self.users).where(and_(self.users.c.login == login, self.users.c.userpass == userpass)))
        return result.fetchone()

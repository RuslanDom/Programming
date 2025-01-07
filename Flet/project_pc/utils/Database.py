from sqlalchemy import create_engine, Table, MetaData, select
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




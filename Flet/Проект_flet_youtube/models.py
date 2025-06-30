from sqlalchemy import Column, Integer, String, Text, VARCHAR, create_engine, MetaData, select, and_, \
    DateTime, insert, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


# Базовый класс для всех таблиц
class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///flet_project.db')
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.metadata = MetaData()
        self.session = self.Session()

db = Database()


class AdminUserTable(db.Base):
    __tablename__ = 'admin_user'
    id = Column(Integer, primary_key=True)
    login = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def to_dict(self):
        """
        Конвертация в словарь
        :return: dict
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def check_email(self, email):
        # result = db.session.execute(select(AdminUser).where(AdminUser.email == email)).fetchone()  # Не конвертируется методом to_dict
        result = db.session.query(AdminUserTable).filter_by(email=email).one_or_none()
        return result

    def check_login(self, login):
        result = db.session.query(AdminUserTable).filter_by(login=login).one_or_none()
        return result

    def insert_new_user(self, login, email, password):
        new_user = AdminUserTable(login=login, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    def check_authorization(self, email, password):
        result = db.session.execute(select(AdminUserTable).where(and_(AdminUserTable.email == email, AdminUserTable.password == password)))
        return result.fetchone()

class PendingPostTable(db.Base):
    __tablename__ = 'pending_post'
    id = Column(Integer, primary_key=True)
    # user_id = Column(Integer, ForeignKey('admin_user.id'))
    message = Column(Text)
    path_image = Column(VARCHAR(255))
    link_post = Column(VARCHAR(255))
    time = Column(DateTime, nullable=False)

    def insert_post(self, message, path_image, link_post, time):
        new_post = PendingPostTable(message=message, path_image=path_image, link_post=link_post, time=time)
        db.session.add(new_post)
        db.session.commit()

    def get_post(self, link):
        result = db.session.query(PendingPostTable).filter_by(link_post=link).one_or_none()
        return result

# if __name__ == '__main__':
#     db.Base.metadata.create_all(db.engine)
#     admin = AdminUser(login='admin', email='ya@ya.com', password='www')
    # Запись в бд
    # db.session.add(admin)
    # db.session.commit()
    # Проверка наличия данного email в бд
    # a = admin.check_email('ya@ya.com')
    # print(a.to_dict())

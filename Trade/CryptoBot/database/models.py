from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, select, delete
from . import DataBase
from sqlalchemy.exc import IntegrityError, ResourceClosedError
import loguru

logger = loguru.logger

class User(DataBase.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    status = Column(Boolean, default=False)
    chat_id = Column(String, unique=True)


class UserHandler(DataBase):
    def __init__(self):
        super().__init__()

    async def get_all_users(self):
        async with self.session.begin():
            result = await self.session.execute(select(User))
            records = result.scalars().all()
            return records

    async def add_user(self, username, password, chat_id, email, status=False):
        try:
            async with self.session.begin():
                user = User(username=username, password=password, chat_id=chat_id, email=email, status=status)
                self.session.add(user)
                await self.session.commit()
                return user
        except IntegrityError as e:
            logger.error("Значение не уникально: {}".format(e))
            return None


    async def get_user(self, username, password):
        try:
            async with self.session.begin():
                user = await self.session.execute(select(User).where(User.username == username and User.password == password))
                user = user.scalars().first()
                return user
        except Exception:
            return None


    async def set_user(self, id, username=None, password=None, email=None):
        try:
            async with self.session.begin():
                resp = await self.session.execute(select(User).where(User.id == id))
                user = resp.scalars().first()
                if username:
                    user.username = username
                elif password:
                    user.password = password
                elif email:
                    user.email = email
                await self.session.commit()
                return user
        except IntegrityError as e:
            logger.error(e)
            return None


    async def set_status_user(self, id, status):
        async with self.session.begin():
            resp = await self.session.execute(select(User).where(User.id == id))
            user = resp.scalars().first()
            user.status = status
            await self.session.commit()
            return user


    async def delete_user(self, id):
        async with self.session.begin():
            await self.session.execute(delete(User).where(User.id == id))
            await self.session.commit()
            return None



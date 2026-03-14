from sqlalchemy import Table, Column, MetaData, Integer, String, ForeignKey, func, text
from database import Base, str_256
from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional, Annotated
import enum, datetime


intpk = Annotated[int, mapped_column(primary_key=True)]
created_add_custom = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_add_custom = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                                onupdate=datetime.datetime.utcnow)]


class WorkerOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    # Упрощение с помощью кастомных типов
    # id: Mapped[intpk]

    username: Mapped[str]


class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class ResumeOrm(Base):
    __tablename__ = 'resume'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    title: Mapped[str_256]
    salary: Mapped[int | None]  # Mapped[Optional[int]] or Mapped[int] = mapped_column(nullable=True)
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    update_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(),
                                                         onupdate=datetime.datetime.now())
    # created_at: Mapped[created_add_custom]
    # update_at: Mapped[updated_add_custom]


















metadata_obj = MetaData()

# Таблица 
workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String)
)








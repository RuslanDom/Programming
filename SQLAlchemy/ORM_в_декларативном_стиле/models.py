import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from config import Base, session


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(DateTime, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # получение списка студентов, которые имеют общежитие.
    @classmethod
    def get_students_with_scholarship(cls):
        students = session.query(Student).filter(cls.scholarship == 1).all()
        students_list = []
        for student in students:
            students_list.append(student.to_json())
        return students_list

    # получение списка студентов, у которых средний балл выше балла переданного входным параметром в функцию.
    @classmethod
    def get_students_average_score(cls, score: float):
        students = session.query(Student).filter(cls.average_score > score).all()
        students_list = []
        for student in students:
            students_list.append(student.to_json())
        return students_list


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime or None, default=None)


    # Счётчик дней задолжности студентов
    @hybrid_property
    def count_days_of_debt(self):
        day = self.date_of_return or datetime.datetime.now()
        count_day = (day - self.date_of_issue).days
        if count_day > 14:
            return {"student_id": self.student_id, "count_day": count_day}
        else:
            return {"student_id": self.student_id, "count_day": "not debt"}

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
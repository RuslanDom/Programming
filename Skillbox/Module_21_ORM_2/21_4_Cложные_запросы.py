from datetime import datetime
import time
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Date, Float, Boolean, func, \
    Subquery
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, backref, joinedload

engine = create_engine('sqlite:///m21_4.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    """
    Таблица книг
    """
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    count = Column(Integer)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    authors = relationship("Author", backref=backref("books", cascade="all, delete-orphan", lazy="select"))

    students = relationship("ReceivingBook", back_populates="book")

    def __repr__(self):
        return f"{self.name}"

class Author(Base):
    """
    Таблица авторов
    """
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)

    def __repr__(self):
        return f"{self.name} {self.surname}"

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    books = relationship("ReceivingBook", back_populates="student")

    def __repr__(self):
        return f"{self.name} {self.surname} {self.phone} {self.email} {self.average_score} {self.scholarship}"



class ReceivingBook(Base):
    """
    Таблица выдачи книг студентам
    """
    __tablename__ = 'receiving_books'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    date_of_issue = Column(DateTime, default=datetime.now())
    date_of_return = Column(DateTime, nullable=True)

    student = relationship("Student", back_populates="books")
    book = relationship("Book", back_populates="students")

    def __repr__(self):
        return f"{self.book_id} {self.author_id}"

    def __repr__(self):
        return f"{self.book_id} {self.author_id}"


def insert_data():
    authors = [
        Author(name= "Александр", surname= "Пушкин"),
        Author(name= "Лев", surname= "Толстой"),
        Author(name= "Михаил", surname= "Булгаков")
    ]
    authors[0].books.extend(
        [
            Book(name="Капитанская дочка", count=5, release_date=datetime.date( 1836, 1, 1)),
            Book(name="Евгений Онегин", count=3, release_date=datetime.date(1838, 1, 1))
        ]
    )
    authors[1].books.extend(
        [
            Book(name="Война и мир", count=10, release_date=datetime.date(1867, 1, 1)),
            Book(name="Анна Каренина", count=7, release_date=datetime.date(1877, 1, 1))
        ]
    )
    authors[2].books.extend(
        [
            Book(name="Морфий", count=5, release_date=datetime.date(1926, 1, 1)),
            Book(name="Собачье сердце", count=3, release_date=datetime.date(1925, 1, 1))
        ]
    )

    students = [
        Student(name="Oleg", surname="Son", phone="3-15-18", email="son@mail.us", average_score="4.5", scholarship=True),
        Student(name="Alex", surname="Krot", phone="3-26-45", email="Krot@gmail.us", average_score="3.9", scholarship=True),
    ]
    session.add_all(authors)
    session.add_all(students)

def give_me_book():
    oleg = session.query(Student).filter(Student.name == "Oleg").one()
    alex = session.query(Student).filter(Student.name == "Alex").one()
    books_for_oleg = session.query(Book).filter(Author.surname == "Толстой", Author.id == Book.author_id).all()
    books_for_alex = session.query(Book).filter(Book.id.in_([1, 3, 4])).all()

    for book in books_for_oleg:
        receiving_book = ReceivingBook()
        receiving_book.book = book
        receiving_book.student = oleg
        session.add(receiving_book)

    for book in books_for_alex:
        receiving_book = ReceivingBook()
        receiving_book.book = book
        receiving_book.student = alex
        session.add(receiving_book)

    session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    check_exist = session.query(Author).all()
    if not check_exist:
        insert_data()
        give_me_book()

    # subquery
    author_q = session.query(Author.id).filter_by(name="Лев").subquery()
    books_by_lev = session.query(Book).filter(Book.author_id.in_(author_q)).all()  # В Subquery есть сокращенный атрибут 'c'
                                                                                   # (что значит columns) к примеру author_id.c.id

    # labels
    students = session.query(Student.name.label('student_name')).all()  # label позволяет определять новый атрибут
                                                                        # к примеру 'student_name', такой колонки в таблице не было
    for student in students:
        if student.student_name == "Oleg":
            print("Oleg")

    # Получим кол-во всех книг в библиотеке с помощью func.sum
    count_of_books = session.query(func.count(Book.count)).scalar()  # scalar - возвращает int

    # Получим кол-во книг по каждому автору с помощью group_by
    # отсортированных по кол-ву по убыванию
    count_books_by_authors = session.query(func.sum(Book.count), Author.name, Author.surname). \
                             filter(Book.author_id == Author.id).group_by(Author.id).order_by(func.sum(Book.count).desc()).all()

    # Использование joinedload - альтернатива lazy = 'joined' ля объекта Query
    # Получаем книги со связанными авторами - жадная загрузка
    books_with_author = session.query(Book).options(joinedload(Book.authors)).all()

    # join двух таблиц
    book_join_author = session.query(Book, Author).join(Book.authors).all()

    # join subquery
    author_q = session.query(Author).filter_by(name="Михаил").subquery()
    michael_books = session.query(Book).filter(Book.author_id == author_q.c.id).all()

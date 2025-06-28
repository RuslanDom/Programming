from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Date, Float, Boolean, Table, func, case
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, backref
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import date, datetime

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///m_21_db.db')
        self.Base = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

db = Database()


class Book(db.Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    # authors = relationship('Author',backref=backref('books',cascade="all, delete-orphan" , lazy="select"))
    authors = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"Book(name={self.name}, count={self.count}, release_date={self.release_date}, author_id={self.author_id})"

class Author(db.Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)

    books = relationship('Book', back_populates='authors', cascade='all, delete-orphan', lazy='select')

    def __repr__(self):
        return f"Author(name={self.name}, surname={self.surname})"

class Student(db.Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    bk_id = relationship('Book', secondary=lambda: students_books)
    books = association_proxy('bk_id', 'id')

    def __repr__(self):
        return (f"Student(name={self.name}, surname={self.surname}, "
                f"phone={self.phone}, email={self.email}, "
                f"average_score={self.average_score}, scholarship={self.scholarship})")

class ReceivingBook(db.Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime, nullable=True)

    students= relationship('Student',backref=backref('receiving_books', lazy="joined", cascade='all, delete-orphan'))
    books = relationship('Book',backref=backref('receiving_books', lazy="subquery", cascade='all, delete-orphan'))

    @hybrid_property
    def count_date_with_book(self):
        days = self.date_of_return or datetime.now()
        delta = (days - self.date_of_issue).days
        return delta

    @count_date_with_book.expression
    def count_date_with_book(cls):
        end_date = case(
            (cls.date_of_return is None, date.today()),
            else_=cls.date_of_return
        )
        return (end_date - cls.date_of_issue).days

    # @hybrid_property
    # def get_month(self):
    #     if self.date_of_issue.month == date.today().month:
    #         return True
    #     return False
    #
    # @get_month.expression
    # def get_month(cls):
    #     return case(
    #             (cls.date_of_issue. == date.today().month, True),
    #             else_=False
    #             )

    def __repr__(self):
        return (f"ReceivingBook(book_id={self.book_id}, student_id={self.student_id}, "
                f"date_of_issue={self.date_of_issue}, date_of_return={self.date_of_return})")


# Integration table
students_books = Table('students_books',
                       db.Base.metadata,
                       Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
                       Column('book_id', Integer, ForeignKey('books.id'), primary_key=True)
                       )


# function insert
def insert_data():
    authors = [
        Author(name= "Александр", surname= "Пушкин"),
        Author(name= "Лев", surname= "Толстой"),
        Author(name= "Михаил", surname= "Булгаков")
    ]
    authors[0].books.extend(
        [
            Book(name="Капитанская дочка", count=5, release_date=date( 1836, 1, 1)),
            Book(name="Евгений Онегин", count=3, release_date=date(1838, 1, 1))
        ]
    )
    authors[1].books.extend(
        [
            Book(name="Война и мир", count=10, release_date=date(1867, 1, 1)),
            Book(name="Анна Каренина", count=7, release_date=date(1877, 1, 1))
        ]
    )
    authors[2].books.extend(
        [
            Book(name="Морфий", count=5, release_date=date(1926, 1, 1)),
            Book(name="Собачье сердце", count=3, release_date=date(1925, 1, 1))
        ]
    )

    students = [
        Student(name="Oleg", surname="Son", phone="3-15-18", email="son@mail.us", average_score=4.5, scholarship=True),
        Student(name="Alex", surname="Krot", phone="3-26-45", email="Krot@gmail.us", average_score=3.9, scholarship=True),
    ]
    db.session.add_all(authors)
    db.session.add_all(students)
    db.session.commit()

def received_books():
    author_query = db.session.query(Author).filter(Author.surname == "Пушкин").subquery()
    books_student_1 = db.session.query(Book).filter(Book.author_id == author_query.c.id).all()
    student_1_query = db.session.query(Student).filter(Student.id == 1).one()
    for book in books_student_1:
        obj = ReceivingBook()
        obj.books = book
        obj.students = student_1_query
        obj.date_of_issue = datetime.now()
        db.session.add(obj)


    books_student_2 = db.session.query(Book).filter(Book.id.in_([4, 5])).all()
    student_2_query = db.session.query(Student).filter(Student.average_score < 4).first()
    for book in books_student_2:
        obj = ReceivingBook()
        obj.books = book
        obj.students = student_2_query
        obj.date_of_issue = datetime.now()
        db.session.add(obj)
    db.session.commit()


# if __name__ == '__main__':
#     try:
#         Base.metadata.create_all(engine)
#         insert_data()
#         received_books()
#         # receiving_request = session.query(ReceivingBook).all()
#         # for record in receiving_request:
#         #     print(record)
#     finally:
#         session.close()
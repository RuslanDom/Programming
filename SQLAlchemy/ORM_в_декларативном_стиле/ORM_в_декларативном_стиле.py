"""
ТЕХЗАДАНИЕ
Задачи
1. Опишите модели с помощью ORM в декларативном стиле. Пока мы не разобрались с зависимостями между таблицами
с помощью ForeignKey - связи между таблицами определять не нужно. Author_id, book_id, student_id - обычные атрибуты
соответствующих таблиц.
2. Определите hybrid_property для таблицы 'receiving_books' - count_date_with_book - количество дней,
которое читатель держит/держал книгу у себя. Подумайте, как определять данный атрибут, если книгу до сих пор не сдали
обратно в библиотеку.
3. Опишите classmethod’ы для таблицы читателей:
    - получение списка студентов, которые имеют общежитие.
    - получение списка студентов, у которых средний балл выше балла переданного входным параметром в функцию.
4. Создайте flask-приложение, в котором опишите роуты:
    - получение всех книг в библиотеке. (GET)
    - получение список должников, которые держат книги у себя более 14 дней. (GET)
    - выдать книгу студенту (POST - входные параметры ID книги и ID студента)
    - сдать книгу в библиотеку (POST - входные параметры ID книги и ID студента, в случае если такой связки нет, выдать ошибку)
5!. Усложнённое задание (по желанию) Создайте роут, с помощью которого будет осуществляться поиск книги по названию.
На вход передается строка, по которой будет осуществляться поиск. Поиск должен выдавать книги,
в названии которых содержится ключевая строка.
"""
import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, declarative_base
from flask import Flask, request, jsonify


app = Flask(__name__)
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


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
        students = session.query(Student).filter(cls.scholarship == True).all()
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
    date_of_return = Column(DateTime)

    @hybrid_property
    def count_date_with_book(self, student_id):
        data = session.query(ReceivingBook).filter_by(student_id=student_id).one_or_none()
        if data:
            if data.date_of_return:
                return data.date_of_return - data.date_of_issue
            else:
                return datetime.date.today() - data.date_of_issue
        else:
            return None

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@app.before_request
def starting_app():
    Base.metadata.create_all(engine)

# получение всех книг в библиотеке. (GET)
@app.route('/books')
def get_all_books():
    books = session.query(Book).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list), 200

@app.route('/books', methods=['POST'])
def add_book():
    name = request.json['name']
    release_date = datetime.date.today()
    author_id = request.json['author_id']

    book = Book(name=name,release_date=release_date,author_id=author_id)
    session.add(book)
    session.commit()
    return jsonify(book.to_json()), 201


# получение список должников, которые держат книги у себя более 14 дней. (GET)
@app.route('/students')
def get_students_received_books():
    students = session.query(Student).all()
    students_list = []
    for student in students:
        days = ReceivingBook().count_date_with_book(student.id)
        if days:
            if days > 14:
                students_list.append(student.to_json())
    return jsonify(students_list), 200

@app.route('/students', methods=['POST'])
def add_student():
    name = request.json['name']
    surname = request.json['surname']
    phone = request.json['phone']
    email = request.json['email']
    average_score = request.json['average_score']
    scholarship = request.json['scholarship']
    student = Student(
        name=name,
        surname=surname,
        phone=phone,
        email=email,
        average_score=average_score,
        scholarship=scholarship
    )
    session.add(student)
    session.commit()
    return jsonify(student.to_json()), 201

# выдать книгу студенту (POST - входные параметры ID книги и ID студента)
@app.route('/receiving_books/get_book', methods=['POST'])
def get_book_in_library():
    book_id = request.form.get('book_id')
    student_id = request.form.get('student_id')
    date_of_issue = datetime.date.today()

    new_received_book = ReceivingBook(book_id=book_id, student_id=student_id, date_of_issue=date_of_issue)
    session.add(new_received_book)
    session.commit()
    return jsonify(new_received_book.to_json()), 201

# сдать книгу в библиотеку (POST - входные параметры ID книги и ID студента, в случае если такой связки нет, выдать ошибку)
@app.route('/receiving_books/return_book', methods=['POST'])
def return_book_in_library():
    book_id = request.form.get('book_id')
    student_id = request.form.get('student_id')
    date_of_return = datetime.date.today()
    book = session.query(ReceivingBook).filter_by(student_id=student_id and book_id).one_or_none()
    if book:
        new_entry_receiving_book = ReceivingBook(
            book_id=book_id,
            student_id=student_id,
            date_of_issue=book.date_of_issue,
            date_of_return=date_of_return
        )
        session.add(new_entry_receiving_book)
        session.commit()
        return jsonify(new_entry_receiving_book.to_json()), 201
    else:
        return {"error": "Такой связки нет"}, 204









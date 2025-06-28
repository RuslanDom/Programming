import os, ast
from flask import Flask, request
from marshmallow import ValidationError
import datetime
from datetime import date
from werkzeug.utils import secure_filename
from models import Author, Student, ReceivingBook, Book, db
from schemas import BookSchema, AuthorSchema, StudentSchema, ReceivedBookSchema
from sqlalchemy import update, func
from typing import List
import csv

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
session = db.session

@app.before_request
def before_request():
    db.Base.metadata.create_all(db.engine)

@app.route('/books', methods=['GET', 'POST'])
def books_endpoint():
    schema = BookSchema()
    if request.method == 'GET':
        all_books = session.query(Book).all()
        return schema.dump(all_books, many=True)
    elif request.method == 'POST':
        try:
            data = request.get_json()
            valid_data = schema.load(data)
            new_book = Book(
                name=valid_data.name,
                author_id=valid_data.author_id,
                release_date=valid_data.release_date,
                count=valid_data.count
            )
            session.add(new_book)
            session.commit()
            return schema.dump(new_book), 201
        except ValidationError as e:
            return {"errors": e.messages}, 400
        finally:
            session.close()
    else:
        return {'message': 'Method not allowed'}, 405

@app.route('/authors', methods=['GET', 'POST'])
def authors_endpoint():
    schema = AuthorSchema()
    if request.method == 'GET':
        all_authors = session.query(Author).all()
        return schema.dump(all_authors, many=True)
    elif request.method == 'POST':
        try:
            data = request.get_json()
            valid_data = schema.load(data)
            new_author = Author(
                name=valid_data.name,
                surname=valid_data.surname
            )
            session.add(new_author)
            session.commit()
            return schema.dump(new_author), 201
        except ValidationError as e:
            return {"errors": e.messages}, 400
        finally:
            session.close()
    else:
        return {'message': 'Method not allowed'}, 405


@app.route('/students', methods=['GET', 'POST'])
def students_endpoint():
    schema = StudentSchema()
    if request.method == 'GET':
        all_students = session.query(Student).all()
        return schema.dump(all_students, many=True)
    elif request.method == 'POST':
        try:
            data = request.get_json()
            valid_data = schema.load(data)
            new_student = Student(
                name=valid_data.name,
                surname=valid_data.surname,
                phone=valid_data.phone,
                email=valid_data.email,
                average_score=valid_data.average_score,
                scholarship=valid_data.scholarship
            )
            session.add(new_student)
            session.commit()
            return schema.dump(new_student), 201
        except ValidationError as e:
            return {"errors": e.messages}, 400
    else:
        return {'message': 'Method not allowed'}, 405

@app.route('/receiving_books', methods=['GET', 'POST'])
def receiving_books_endpoint():
    schema = ReceivedBookSchema()
    if request.method == 'GET':
        all_records = session.query(ReceivingBook).all()
        return schema.dump(all_records, many=True)
    elif request.method == 'POST':
        try:
            data = request.get_json()
            valid_data = schema.load(data)
            new_record = ReceivingBook(
                book_id=valid_data.book_id,
                student_id=valid_data.student_id,
                date_of_issue=valid_data.date_of_issue
            )
            session.add(new_record)
            book = session.query(Book).filter(Book.id == valid_data.book_id).first()
            book.count -= 1
            session.commit()
            return schema.dump(new_record), 201
        except ValidationError as e:
            return {"errors": e.messages}, 400
        finally:
            session.close()
    else:
        return {'message': 'Method not allowed'}, 405


@app.route("/receiving_books/return_book", methods=['POST'])
def receiving_books_return():
    if request.method == 'POST':
        try:
            data = request.get_json()
            return_book = session.query(ReceivingBook).filter(ReceivingBook.book_id == data["book_id"],
                                                              ReceivingBook.student_id == data["student_id"]).one_or_none()

            if return_book:
                date_of_return = datetime.date(2025, 6, 20)
                session.execute(update(ReceivingBook).where(ReceivingBook.id == return_book.id).values(date_of_return=date_of_return))
                book = session.query(Book).filter(Book.id == return_book.book_id).first()
                book.count += 1
                session.commit()
                return return_book, 201
        finally:
            session.close()
    else:
        return {'message': 'Method not allowed'}, 405


@app.route("/debtors", methods=['GET'])
def get_debtors_endpoint():
    schema = StudentSchema()
    if request.method == 'GET':
        debtors_list: List[int] = []
        data_records = session.query(ReceivingBook).all()
        for debtor in data_records:
            if debtor.count_date_with_book > 1:
                debtors_list.append(debtor.student_id)
        debtors_students = session.query(Student).filter(Student.id.in_(debtors_list)).all()
        return schema.dump(debtors_students, many=True), 200
    else:
        return {'message': 'Method not allowed'}, 405


@app.route("/books/name/<string:name>")
def find_books_by_name(name):
    schema = BookSchema()
    if request.method == 'GET':
        books = session.query(Book).filter(Book.name.like("%" + name + "%")).all()
        return schema.dump(books, many=True), 200
    else:
        return {'message': 'Method not allowed'}, 405


@app.route("/books/author_id/<int:id>", methods=['GET'])
def find_books_by_author_id(id: int):
    """
    получить кол-во оставшихся в библиотеке книг по автору (GET -входной параметр - ID автора)
    :param id: int
    :return: Список книг
    """
    schema = BookSchema()
    if request.method == "GET":
        books = session.query(Book).filter(Book.author_id == id, Book.count > 0).all()
        return schema.dump(books, many=True), 200
    else:
        return {'message': 'Method not allowed'}, 405



@app.route("/books/student_id/<int:id>", methods=['GET'])
def get_books_that_the_student_has_not_read(id: int):
    """
    Получить список книг, которые студент не читал, при этом другие книги этого автора студент уже брал
    (GET - входной параметр - ID студента). Пример: Я брал книгу Льва Толстого “Война и мир”, роут должен
    вернуть другие произведения этого автора, которые есть в библиотеке
    """
    schema = BookSchema()
    if request.method == "GET":
        student_has_read_books = session.query(ReceivingBook.book_id).filter_by(student_id=id).subquery()
        books_authors_id = session.query(Book).filter(Book.id.in_(student_has_read_books)).all()
        books = session.query(Book).filter(
            Book.author_id.in_(b.author_id for b in books_authors_id),
            Book.id.not_in(b.id for b in books_authors_id)
            ).all()
        return schema.dump(books, many=True), 200
    else:
        return {'message': 'Method not allowed'}, 405



@app.route("/receiving_books/avg_books", methods=["GET"])
def get_avg_received_books():
    """
    получить среднее кол-во книг, которые студенты брали в этом месяце (GET)
    :return: float
    """
    received_books = session.query(func.count(ReceivingBook.book_id)).filter(func.extract("month", ReceivingBook.date_of_issue).label("month") == date.today().month).all()
    student = session.query(func.count(ReceivingBook.student_id)).group_by(ReceivingBook.student_id).all()
    return {"average_count": received_books[0][0] / student[0][0]}, 200


# получить самую популярную книгу среди студентов, у которых средний балл больше 4.0 (GET)
@app.route("/books/popular", methods=["GET"])
def the_most_popular_book():
    schema = BookSchema()
    if request.method == "GET":
        # sub_request = (session.query(ReceivingBook.book_id, func.count(ReceivingBook.book_id).label("ccc")).join(ReceivingBook.students).
        #                filter(Student.average_score > 4.0).group_by(ReceivingBook.book_id).subquery())
        # result = session.query(Book).join(sub_request).filter(sub_request.c.book_id == Book.id).order_by(sub_request.c.ccc.desc()).first()
        result = (session.query(Book).join(ReceivingBook.students).join(ReceivingBook.books).
                  filter(Student.average_score > 4.0).group_by(ReceivingBook.book_id).
                  order_by(func.count(ReceivingBook.book_id).desc()).first())
        return schema.dump(result), 200
    else:
        return {"message": "Method not allowed"}, 405


# получить ТОП-10 самых читающих студентов в этом году (GET)
@app.route("/students/top", methods=["GET"])
def top_students():
    schema = StudentSchema()
    if request.method == "GET":
        students = (session.query(Student).join(ReceivingBook.students).group_by(ReceivingBook.student_id).
                    order_by(func.count(ReceivingBook.student_id).desc()).limit(10).all())
        return schema.dump(students, many=True), 200
    else:
        return {"message": "Method not allowed"}, 405

# 3. Создайте роут, который будет принимать csv-файл с данными по студентам (разделитель ;). Используя
# csv.DictReader (https://docs.python.org/3/library/csv.html#csv.DictReader),
# обработайте файл и используйте Session.bulk_insert_mappings() для массовой вставки студентов.
@app.route("/students/add_many", methods=["POST"])
def add_many_students():
    schema = StudentSchema()
    if request.method == "POST":
        data = request.files.get("filename")
        csvfile = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(data.filename))
        with open(csvfile, newline="", encoding="utf-8") as csv_f:
            reader = csv.DictReader(csv_f)
            result = []
            for row in reader:
                row["average_score"] = float(row["average_score"])
                row["scholarship"] = ast.literal_eval(row["scholarship"])
                result.append(row)
            session.bulk_insert_mappings(Student, result)
            session.commit()
        students = session.query(Student).all()
        return schema.dump(students, many=True), 200


    else:
        return {"message": "Method not allowed"}, 405


# 4. По желанию. Создайте триггер на событие перед вставкой в таблицу students.
# Триггер должен проверять, что номер телефона имеет формат +7(9**) -*** - ** - **, где * - цифра от 0 до 9.

if __name__ == '__main__':
    app.run(debug=True)

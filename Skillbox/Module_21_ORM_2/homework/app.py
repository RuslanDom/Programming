from flask import Flask, request
from marshmallow import ValidationError
import datetime
from models import Author, Student, ReceivingBook, Book, Base, engine, session
from schemas import BookSchema, AuthorSchema, StudentSchema, ReceivedBookSchema
from sqlalchemy import update

app = Flask(__name__)

@app.before_request
def before_request():
    Base.metadata.create_all(engine)

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
            return schema.dump(new_book)
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
            return schema.dump(new_author)
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
            return schema.dump(new_student)
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
            return schema.dump(new_record)
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
                return {"message": "Success"}
        finally:
            session.close()


# получить кол-во оставшихся в библиотеке книг по автору (GET -входной параметр - ID автора)

if __name__ == '__main__':
    app.run(debug=True)
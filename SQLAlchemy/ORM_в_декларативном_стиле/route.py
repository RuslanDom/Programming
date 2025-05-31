import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float, Boolean, update
from flask import request, jsonify
from config import app, Base, engine, session
from models import Student, Book, ReceivingBook, Author

@app.before_request
def starting_app():
    Base.metadata.create_all(engine)

# получение всех книг в библиотеке. (GET)
@app.route('/books', methods=['GET', 'POST'])
def book_endpoint():
    if request.method == 'GET':
        books = session.query(Book).all()
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        session.close()
        return jsonify(books_list), 200
    elif request.method == 'POST':
        name = request.form.get('name')
        release_date = datetime.datetime.strptime(request.form.get('release_date'), '%Y-%m-%d')
        author_id = request.form.get('author_id')
        count = request.form.get('count')

        book = Book(name=name,release_date=release_date, author_id=author_id, count=count)
        session.add(book)
        session.commit()
        return jsonify(book.to_json()), 201



@app.route('/students', methods=['GET', 'POST'])
def student_endpoint():
    if request.method == 'GET':
        students = session.query(Student).all()
        students_list = []
        for student in students:
            students_list.append(student.to_json())
        session.close()
        return jsonify(students_list), 200
    elif request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        average_score = request.form.get('average_score')
        scholarship = request.form.get('scholarship')
        student = Student(
            name=name,
            surname=surname,
            phone=phone,
            email=email,
            average_score=average_score,
            scholarship=int(scholarship)
        )
        session.add(student)
        session.commit()
        return jsonify(student.to_json()), 201


@app.route('/authors', methods=['GET', 'POST'])
def authors_endpoint():
    if request.method == 'GET':
        authors = session.query(Author).all()
        authors_list = []
        for author in authors:
            authors_list.append(author.to_json())
        session.close()
        return jsonify(authors_list), 200
    elif request.method == 'POST':
        name = request.form.get("name")
        surname = request.form.get("surname")
        new_author = Author(name=name, surname=surname)
        session.add(new_author)
        session.commit()
        return jsonify(new_author.to_json()), 201

@app.route("/receiving_books", methods=['GET', 'POST'])
def receiving_books_endpoint():
    if request.method == 'GET':
        receiving_books = session.query(ReceivingBook).all()
        receiving_books_list = []
        for receiving_book in receiving_books:
            receiving_books_list.append(receiving_book.to_json())
            session.close()
        return jsonify(receiving_books_list), 200
    elif request.method == 'POST':
        book_id = request.form.get('book_id')
        student_id = request.form.get('student_id')
        date_of_issue = datetime.datetime.strptime(request.form.get('date_of_issue'), "%Y-%m-%d")
        order = session.query(ReceivingBook).filter_by(book_id=book_id, student_id=student_id).one_or_none()
        if order and not order.date_of_return:
            return {"error": "Эту книгу ещё не вернул студент"}, 200
        elif order and order.date_of_return:
            session.delete(order)
        new_received_book = ReceivingBook(book_id=book_id, student_id=student_id, date_of_issue=date_of_issue)
        session.add(new_received_book)
        session.commit()
        book = session.query(Book).filter_by(id=book_id).one_or_none()
        session.execute(update(Book).where(Book.id == book_id).values(count=book.count - 1))
        session.commit()
        return jsonify(new_received_book.to_json()), 201


# выдать книгу студенту (POST - входные параметры ID книги и ID студента)

# сдать книгу в библиотеку (POST - входные параметры ID книги и ID студента, в случае если такой связки нет, выдать ошибку)
@app.route('/receiving_books/return_book', methods=['POST'])
def return_book_in_library():
    book_id = request.form.get('book_id')
    student_id = request.form.get('student_id')
    date_of_return = datetime.datetime.strptime(request.form.get('date_of_return'), "%Y-%m-%d")
    order = session.query(ReceivingBook).filter_by(student_id=student_id, book_id=book_id).one_or_none()
    if order:
        new_entry_receiving_book = ReceivingBook(
            book_id=order.book_id,
            student_id=order.student_id,
            date_of_issue=order.date_of_issue,
            date_of_return=date_of_return
        )
        order.date_of_return = date_of_return
        session.commit()
        book = session.query(Book).filter_by(id=book_id).one_or_none()
        # book.count += 1
        session.execute(update(Book).where(Book.id == book_id).values(count=book.count + 1))
        session.commit()
        return jsonify(new_entry_receiving_book.to_json()), 200
    else:
        session.close()
        return {"error": "Такой связки нет"}, 204

# получение список должников, которые держат книги у себя более 14 дней. (GET)
@app.route('/debtors', methods=['GET'])
def debtors_endpoint():
    receiving_books = session.query(ReceivingBook).all()
    debtors_list = []
    for book in receiving_books:
        days = book.count_date_with_book()
        if days:
            if days > 14:
                debtors_list.append(session.query(Student).filter(Student.id == book.student_id).one())
    session.close()
    return jsonify(debtors_list), 200


if __name__ == '__main__':
    app.run(debug=True)
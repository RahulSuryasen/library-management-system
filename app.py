from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

DATABASE = 'library.db'

# Utility function to connect to the database
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to display all books
@app.route('/books')
def books():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return render_template('books.html', books=books)

# Route for adding a new book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()
        conn.close()
        
        flash('Book added successfully!', 'success')
        return redirect(url_for('books'))
    return render_template('add_book.html')

# Route for editing a book (optional)
@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (title, author, book_id))
        conn.commit()
        conn.close()
        flash('Book updated successfully!', 'success')
        return redirect(url_for('books'))

    conn.close()
    return render_template('edit_book.html', book=book)

# Route for deleting a book
@app.route('/delete_book/<int:book_id>', methods=['GET'])
def delete_book(book_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    flash('Book deleted successfully!', 'danger')
    return redirect(url_for('books'))

if __name__ == '__main__':
    app.run(debug=True)

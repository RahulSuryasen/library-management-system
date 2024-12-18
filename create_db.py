import sqlite3

# Create database and books table if not exists
DATABASE = 'library.db'

def create_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create the books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

create_db()

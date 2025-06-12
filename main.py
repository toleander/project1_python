# connect DB
import sqlite3

conn = sqlite3.connect('library.db')

cursor = conn.cursor()

# create table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER DEFAULT NULL
    );
    """
)

# add new book
cursor.execute(
    """
    INSERT INTO books (title, author, year) 
    VALUES (?, ?, ?);
    """,
    ("Leviathan Wakes", "James Corey", 2011)
)

# add another book
cursor.execute(
    """
   INSERT INTO books (title, author, year) 
    VALUES (?, ?, ?);
    """,
    ("Caliban's War", "James Corey", 2012)
)

# add another book
cursor.execute(
    """
   INSERT INTO books (title, author, year) 
    VALUES (?, ?, ?);
    """,
    ("Cibola Burn", "James Corey", 2014)
)

conn.commit()

# delete books if more than 3
cursor.execute(
    """
   DELETE FROM books  
    WHERE id>3;
    """,
)

# get all books
print(
    cursor.execute(
        """SELECT * FROM books;"""
    ).fetchall()
)



# close DB connection
cursor.close()
conn.close()

#!/usr/bin/python3
import sqlite3
"""
The Engineering Part of the BookStore
"""

def connect():
    """
    Function creates connection to the database
    """
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BookStore (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()


def view():
    """
    Function list items of the database
    """
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BookStore")
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        return row

def search():
    pass


def add(title, author, year, isbn):
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO BookStore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def update(id, title="", author="", year="", isbn=""):
    conn = sqlite3.connect("BookStore.db")
    cur = conn.cursor()
    cur.execute("UPDATE BookStore SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


def delete():
    pass


def close():
    pass


connect()
# view()
search()
add("Believer's Authority", "Kenneth E. Hagin", 1980, 73773737373)
update(1)
# delete()
# close()
view()

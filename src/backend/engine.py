#!/usr/bin/python3
import sqlite3
"""
The Engineering Part of the BookStore
"""

def connect():
    """
    Function creates connection to the database
    """
    conn = sqlite3.connect("EmyBookStore.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BookStore (id INTEGER PRIMARY KEY, author text, title text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def view():
    """
    Function list items of the database
    """
    conn = sqlite3.connect("EmyBookStore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BookStore")
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        return row


def search(title="", author="", year="", isbn=""):
    """
    Searches for Specified iem
    """
    conn = sqlite3.connect("EmyBookStore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BookStore WHERE title=? OR author=? OR year=? OR isbn", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        return row


def add(title, author, year, isbn):
    conn = sqlite3.connect("EmyBookStore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO BookStore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("EmyBookStore.db")
    cur = conn.cursor()
    cur.execute("UPDATE BookStore SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("EmyBookStore.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM BookStore WHERE id=?", (id,))
    conn.commit()
    conn.close()

def close():
    pass


connect()
# view()
# search("Kenneth E. Hagin")
add("Believer's Authority", "Kenneth E. Hagin", 1980, 73773737373)
add("Believer's Love Walk", "Kenneth E. Hagin", 1983, 783-3-73737373)
# update(1)
# delete(1)
# close()
view()

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
    cur.execute("CREATE TABLE IF NOT EXISTS BookStore (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
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
    for i in range(len(rows)):
        print(rows[i])

def search(title="", author="", year="", isbn=""):
    """
    Searches for Specified iem
    """
    conn = sqlite3.connect("EmyBookStore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM BookStore WHERE title=? OR author=? OR year=? OR isbn", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    for i in range(len(rows)):
        print(rows[i])


def add(title, author, year, isbn):
    conn = sqlite3.connect("EmyBookStore.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO BookStore VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def update(id, title="", author="", year="", isbn=""):
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
# search("Believer's Authority", "Kenneth E. Hagin", 1980, 73773737373)
# add("Believer's Authority", 'Kenneth E. Hagin', 1980, 73773737373)
# add("Believer's Love Walk", 'Kenneth E. Hagin', 1983, 30736593)
# add('The Anointing', 'Kenneth E. Hagin', 1960, 12455673)
# add('Healing', 'Kenneth E. Hagin', 1965, 334567213)
# add('Tongues Beyond Upper Room', 'Kenneth E. Hagin', 1995, 237213)
# add('How To Be Led By The Spirit', 'Kenneth E. Hagin', 1960, 3445446)
# delete(7)
# close()
# update(7, "The Triumphant Church", 'Kenneth E. Hagin', 1960, 3445446)
view()

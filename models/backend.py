#!/usr/bin/python3
import sqlite3
"""
The Engineering Part of the BookStore
"""

class dbModel():
    """
    Class Connect and Perform defined Methods
    """
    def __init__(self, conn, cur):
        """
        Initializing, creates connection to the database
        and create table
        """
        self.conn = conn
        self.cur = cur
        self.cur.execute("CREATE TABLE IF NOT EXISTS BookStore "
                         "(id INTEGER PRIMARY KEY, title text, "
                    "author text, year integer, isbn integer)")
        self.conn.commit()


    def view(self):
        """
        Method lists items of the database
        """
        self.cur.execute("SELECT * FROM BookStore")
        self.rows = self.cur.fetchall()
        return self.rows


    def search(self, title="", author="", year="", isbn=""):
        """
        Method searches for Specified item
        """
        self.cur.execute("SELECT * FROM BookStore WHERE title=? "
                    "OR author=? OR year=? OR isbn=?",
                    (title, author, year, isbn))
        self.rows = self.cur.fetchall()
        return self.rows


    def add(self, title, author, year, isbn):
        """
        Method adds entry to the database
        """
        self.cur.execute("INSERT INTO BookStore "
                    "VALUES (NULL, ?, ?, ?, ?)",
                    (title, author, year, isbn))
        self.conn.commit()


    def update(self, id, title="", author="", year="", isbn=""):
        """
        Method updates existing data
        """
        self.cur.execute("UPDATE BookStore SET title=?, author=?, year=?, "
                    "isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()


    def delete(self, id):
        """
        Method deletse specified data
        """
        self.cur.execute("DELETE FROM BookStore WHERE id=?", (id,))
        self.conn.commit()


# conn = sqlite3.connect(".EmyBookStore.db")
# cur = conn.cursor()
# db = dbModel(conn, cur)

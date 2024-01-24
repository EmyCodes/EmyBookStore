#!/usr/bin/python3
import sqlite3
"""
The Engineering Part of BookStore
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

connect()


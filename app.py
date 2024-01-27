#!/usr/bin/python3
import sqlite3
from tkinter import *

from models import dbModel

"""
GUI of BookStore

HAS ENTRY:\n
    Title\n
    Author\n
    Year\n
    ISBN\n

HAS BUTTON:\n
    View\n
    Search Entry\n
    Add Entry\n
    Update Selected\n
    Delete Selected\n
    Close
"""


# Create Connection to db
conn = sqlite3.connect(".EmyBookStore.db")
cur = conn.cursor()
db = dbModel(conn, cur)


def get_selected_row(event):
    """
    Returns list of selected row
    """
    global selected_tuple
    index = list_box1.curselection()[0]
    selected_tuple = list_box1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_all():
    """View command"""
    list_box1.delete(0, END)
    for row in db.view():
        list_box1.insert(END, row)


def add_command():
    db.add(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box1.delete(0, END)
    list_box1.insert(END, (title_text.get(), author_text.get(),
                           year_text.get(), isbn_text.get()))


def update_command():
    """update command"""
    list_box1.delete(0, END)
    id = selected_tuple[0]
    db.update(id, title_text.get(), author_text.get(),
           year_text.get(), isbn_text.get())
    list_box1.insert(END, (id, title_text.get(), author_text.get(),
                           year_text.get(), isbn_text.get()))


def delete_command():
    db.delete(selected_tuple[0])
    list_box1.delete(0, END)
    for row in db.view():
        list_box1.insert(END, row)


def search_command():
    """Search command"""
    list_box1.delete(0, END)
    rows = db.search(title_text.get(), author_text.get(),
                  year_text.get(), isbn_text.get())
    if len(rows) == 0:
        list_box1.insert(END, "No records")
    for row in rows:
        list_box1.insert(END, row)


def close_commaand():
    """Close command"""
    conn.close()
    window.destroy()


window = Tk()


window.wm_title("EmyBookStore")

# Labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Entry
title_text = StringVar()
e1 = Entry(window, textvariable=title_text, border=2)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text, border=2)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text, border=2)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text, border=2)
e4.grid(row=1, column=3)

# Buttons
b1 = Button(window, text="View all", width=12, border=3, command=view_all)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12,
            border=3, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12,
            border=3, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12,
            border=3, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12,
            border=3, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, border=3, command=close_commaand)
b6.grid(row=7, column=3)

# ListBox
list_box1 = Listbox(window, height=6, width=35, border=2)
list_box1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window, width=15)
sb1.grid(row=2, column=2, rowspan=6)

list_box1.config(yscrollcommand=sb1.set)
sb1.config(command=list_box1.yview)
list_box1.bind("<<ListboxSelect>>", get_selected_row)

__copyright = Label(window, text="(C) EmyCodes 2024")
__copyright.grid(row=7, column=1, columnspan=2)

window.mainloop()

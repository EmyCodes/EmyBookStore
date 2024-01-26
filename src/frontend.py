#!/usr/bin/python3
from tkinter import *

from models.backend import add, update, delete, search, view
from settings import *

"""
GUI of BookStore

HAS ENTRY:
    Title
    Author
    Year
    ISBN

HAS BUTTON;
    View
    Search Entry
    Add Entry
    Update Selected
    Delete Selected
    Close
"""


def get_selected_row(event):
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
    list_box1.delete(0, END)
    for row in view():
        list_box1.insert(END, row)
    # list_box1.insert(END, f"{len(view())}")


def add_command():
    add(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box1.delete(0, END)
    list_box1.insert(END, (title_text.get(), author_text.get(),
                           year_text.get(), isbn_text.get()))


def update_command():
    list_box1.delete(0, END)
    id = selected_tuple[0]
    update(id, title_text.get(), author_text.get(),
           year_text.get(), isbn_text.get())
    list_box1.insert(END, (id, title_text.get(), author_text.get(),
                           year_text.get(), isbn_text.get()))


def delete_command():
    delete(selected_tuple[0])
    list_box1.delete(0, END)
    for row in view():
        list_box1.insert(END, row)


def search_command():
    list_box1.delete(0, END)
    rows = search(title_text.get(), author_text.get(),
                  year_text.get(), isbn_text.get())
    if len(rows) == 0:
        list_box1.insert(END, "No records")
    for row in rows:
        list_box1.insert(END, row)



#!/usr/bin/python3
from tkinter import *
# from frontend import view_all
from src import (
    get_selected_row, add_command, delete_command, update_command,
    search_command, view_all
)

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

b6 = Button(window, text="Close", width=12, border=3, command=window.destroy)
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

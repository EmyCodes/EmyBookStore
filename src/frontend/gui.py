#!/usr/bin/python3
from tkinter import *
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

window = Tk()

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
e1 = Entry(window)
e1.grid(row=0, column=1)

e2 = Entry(window)
e2.grid(row=0, column=3)

e3 = Entry(window)
e3.grid(row=1, column=1)

e4 = Entry(window)
e4.grid(row=1, column=3)

# Buttons
b1 = Button(window, text="View all")
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry")
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry")
b3.grid(row=4, column=3)

b4 = Button(window, text="Update")
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete")
b5.grid(row=6, column=3)

b6 = Button(window, text="Close")
b6.grid(row=7, column=3)

window.mainloop()
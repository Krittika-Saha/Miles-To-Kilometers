from tkinter import Entry, Label, Tk, Button
from math import ceil

window = Tk()
window.title("Widget Examples")
window.minsize(width=350, height=75)
window.config(padx=30, pady=20)

#Button Actions

def button_clicked():
  result.configure(text=ceil(int(entry.get())*1.609))
  
#is equal to label

is_equal = Label(text='is equal to')
is_equal.grid(column=0, row=2, pady=10)

#Entry

entry = Entry(width=10)
entry.grid(column=1, row=1)


#Result

result = Label(text='0')
result.grid(column=1, row=2, padx=20)


#Button

button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=3)


#Miles

miles = Label(text='Miles')
miles.grid(column=2, row=1)

#Km

km = Label(text='km')
km.grid(column=2, row=2)
window.mainloop()

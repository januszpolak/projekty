#!/usr/bin/python3

from tkinter import *
import datetime

window = Tk()

window.title("Data i godzina")
window.geometry('500x100')

date = datetime.datetime.now()
date1 = date.strftime("%d/%m/%Y")
date2 = date.strftime("%H:%M") 

label = Label(window, text=date1, font=("Arial Bold", 32))
label.grid(column=0, row=0)

label = Label(window, text='      ', font=("Arial Bold", 32))
label.grid(column=1, row=0)

label = Label(window, text=date2, font=("Arial Bold", 32))
label.grid(column=2, row=0)


window.mainloop()






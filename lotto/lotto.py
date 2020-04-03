#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import random
from random import randint
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Losowanie 6 liczb TOTOLOTEK')
root.geometry('600x500')
root.configure(background="#007799")

background_image = PhotoImage(file="l.gif")

background = Label(root, image=background_image, bd=0)
background.pack()

var = 'Proponowne liczby TOTOLOTKA to: '
value = random.sample(range(1,49), 6)


print(value)
l = Label(root, width=50, text=var, font=("Sans-serif", 20), bg="yellow")
l.pack(side=TOP)
w = Label(root, width=50, text=value, font=("Impact", 25), bg="yellow")
w.pack(side=BOTTOM)
   

root.mainloop()

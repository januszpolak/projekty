#!/usr/bin/env python3

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from mpyg321.mpyg321 import MPyg321Player

okno = tk.Tk()
okno.title('Otwieracz plików :))')
okno.geometry('600x200')


def browse():
    global player
    file = filedialog.askopenfilename(initialdir = '/home/jpolak/Muzyka')
    player = MPyg321Player()
    player.play_song(file)

    global napis
    napis = Label(okno)
    napis.config(text=file.strip('/home/jpolak/Muzyka'))
    napis.grid(column=0, row=1)
      
def stop():
    player.stop()
    napis.config(text='Brak pliku')

btn = Button(okno, text='Kliknij by otworzyć ...', command=browse)
btn.grid(column=0, row=0)

btn1 = Button(okno, text='Stop', command=stop)
btn1.grid(column=0, row=3)

okno.mainloop()


#!/usr/bin/env python3

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import vlc


okno = tk.Tk()
okno.title('Otwieracz plików :))')
okno.geometry('600x200')


def browse():
    global player
    file = filedialog.askopenfilename(initialdir = '/home/jpolak/Muzyka')
    player = vlc.MediaPlayer(file)
    player.play()

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


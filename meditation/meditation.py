#!/usr/bin/python3

from tkinter import *
import tkinter as tk
from mpyg321.mpyg321 import MPyg321Player
from PIL import ImageTk,Image
import time
import os


player = MPyg321Player()

def rain():
    player.play_song('rain.mp3')


def beach():
    player.play_song('beach.mp3')


def stop():
    player.stop()
    

root = tk.Tk()
root.title("Meditation App")
root.resizable(False, False)


canvas = tk.Canvas(root, width=450, height=250)
canvas.pack()

photo = PhotoImage(file='medit.png')
canvas.create_image(20,5, image=photo, anchor=NW)


button_rain = tk.Button(root, text='Rain', bg='red', fg='white', command=rain)
button_rain.pack(side='left')


button_beach = tk.Button(root, text='Beach', bg='red', fg='white', command=beach)
button_beach.pack(side='left')


button_stop = tk.Button(root, text='Stop', bg='red', fg='white', command=stop)
button_stop.pack(side='left')


button_quit = Button(root, text='Exit', bg='red', command=root.destroy)
button_quit.pack(side='right')


root.mainloop()

#!/usr/bin/python3

from tkinter import *
from configparser import ConfigParser
from playsound import playsound


root = Tk()
root.geometry('400x250')
root.title('Login Panel')
root.configure(background='#a33540')

# storage login and password in different config file -- config.ini
config = ConfigParser()
config.read('config.ini')
login = config['DEFAULT']['login']
password = config['DEFAULT']['password']

get_in = 'Brawo !!! Udało się, wchodzisz :))'
get_out = 'Podaj prawidłowy login i hasło, aby wejść ... '

def update():
    label1.delete('1.0', END)


def check():
    if login_input.get() == login and pass_input.get() == password:
        update()
        label1.insert(INSERT, get_in)
        playsound('appl.mp3')
        
    else:
        update()
        label1.insert(INSERT, get_out)
        playsound('evil.wav')


label = Label(root, text='Wpisz login i hasło ...', bg='#a33540', font=30, pady=25)
label.pack()

login_input = Entry(root, width=20, bd=3)
login_input.pack()

pass_input = Entry(root, width=20, bd=3, show='*')
pass_input.pack()

btn = Button(root, text='Potwierdź', command=check)
btn.pack()

label1 = Text(root, bg='white')
label1.pack()



#!/usr/bin/python3

from tkinter import *
from playsound import playsound


root = Tk()
root.geometry('400x250')
root.title('Login to HELL :))')
root.configure(background='#a33540')


login = 'janusz'
password = 'dawajneta'
ble1 = 'Wchodzisz do piekła :))'
ble2 = 'Znajdz prawdziwy login i hasło, aby wejść ... '

def update():
    label1.delete('1.0', END)


def check():
    if login_input.get() == login and pass_input.get() == password:
        update()
        label1.insert(INSERT, ble1)
        playsound('appl.mp3')
        
    else:
        update()
        label1.insert(INSERT, ble2)
        playsound('evil.wav')

label = Label(root, text='Wpisz login i hasło ...', bg='#a33540', font=30, pady=25)
label.pack()

login_input = Entry(root, width=20, bd=3)
login_input.pack()

pass_input = Entry(root, width=20, bd=3, show='*')
pass_input.pack()

btn = Button(root, text='Submit', command=check)
btn.pack()

label1 = Text(root, bg='white')
label1.pack()



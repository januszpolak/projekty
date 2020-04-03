#!/usr/bin/python3

from tkinter import *
import random

root = Tk()
root.geometry('300x600')
root.configure(background='#fce38a')
root.title('TODO APP')


tasks = []

def clear_listbox():
    listbox.delete(0, END)

def update_tasks():
    clear_listbox()
    for task in tasks:
        listbox.insert(END, task)
    

def add_task():
    task = txt_input.get()
    tasks.append(task)
    update_tasks()

def del_one():
    task = listbox.get(ACTIVE)
    if task in tasks:
        tasks.remove(task)
    update_tasks()

    
def delete_all():
    global tasks
    tasks = []
    update_tasks()


    
    





title = Label(root, text='Wpisz zadanie do zrobienia', bg='white',).pack()
txt_input = Entry(root, width=35)
txt_input.pack()
btn_add = Button(root, text='Dodaj zadanie', height=3, bd=5, command=add_task).pack()
btn_rem = Button(root, text='Usuń zadanie', height=3, bd=5, command=del_one).pack()
btn_rem_all = Button(root, text='Usuń wszystkie zadania', height=3, bd=5, command=delete_all).pack()
listbox = Listbox(root, width=35)
listbox.pack()
btn_quit = Button(root, text='Wyjsćie z programu', bg='red', command=root.destroy, bd=5).pack()
root.mainloop()


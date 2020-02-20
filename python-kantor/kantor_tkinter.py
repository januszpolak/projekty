#!/usr/bin/env python3

from tkinter import *
import requests
from bs4 import BeautifulSoup
import datetime


date = datetime.datetime.now()

url = requests.get('http://www.kantorvabanque.pl/')
soup = BeautifulSoup(url.content, 'html.parser')
exchange = soup.find('tbody').get_text()


root = Tk()
root.geometry('600x600')
root.title('Login Panel')
root.configure(background='#a33540')


label = Label(root, text=f'Aktualne kursy walut\nz dnia {date.strftime("%d/%m/%Y")} z godziny {date.strftime("%H:%M")}\nźródło: www.kantorvabanque.pl', bg='#a33540', font=30, pady=25)
label.pack()
label1 = Text(root, bg='white')
label1.pack()
label1.insert(INSERT, exchange)







root.mainloop()

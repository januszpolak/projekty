#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import mysql.connector
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="bitcoin"
)


url = requests.get('https://tokeneo.com/pl/kryptowaluty/bitcoin/')
soup = BeautifulSoup(url.content, 'html.parser')
coin_price = soup.find_all('p')[1].text
print(coin_price)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO actual_prices VALUES(null,null,?)", (coin_price))
mycursor.execute("SELECT * FROM actual_prices")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.commit()  
mydb.close()

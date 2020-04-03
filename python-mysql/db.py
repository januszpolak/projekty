#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="helion"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee")


myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
mydb.close()

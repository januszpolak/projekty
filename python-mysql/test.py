#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3
 
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

#cursor.execute('CREATE TABLE names(id INT PRIMARY KEY, name TEXT, surmane TEXT)')
#cursor.execute('INSERT INTO names VALUES(?,?,?)',(1,'Tomasz', 'Nowak'))
cursor.execute('SELECT * FROM names')

result = cursor.fetchall()

for x in result:
  print(x)


conn.commit()
conn.close()

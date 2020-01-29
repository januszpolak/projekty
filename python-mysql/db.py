import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="janusz"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM spotkanie")


myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
mydb.close()

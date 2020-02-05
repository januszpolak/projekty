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
price = soup.find_all('p')[1].text
print(price)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO prices(prices) values (18000)")
mycursor.execute("SELECT * FROM prices")


myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
mydb.close()

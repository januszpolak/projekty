import requests
from bs4 import BeautifulSoup
import datetime
import matplotlib.pyplot as plt
import numpy as np


date = datetime.datetime.now()

url = requests.get('https://tokeneo.com/pl/kryptowaluty/bitcoin/')
soup = BeautifulSoup(url.content, 'html.parser')


price = soup.find_all('p')[0].text
print(f'Aktualna cena bitcoina wynosi {price}')

with open("btc.txt", "a") as f:
     f.write(price)
     f.write('\n')

     
plt.scatter(1, price)

plt.show()

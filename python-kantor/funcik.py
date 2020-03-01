#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup

url = requests.get('http://www.kantorvabanque.pl/')
soup = BeautifulSoup(url.content, 'html.parser')
buy = soup.find_all('td')[10].get_text()
sell = soup.find_all('td')[11].get_text()
print(f'Skup funta po: {buy} zł')
print(f'Sprzedaż funta po: {sell} zł\n')
print('--- Żródło http://www.kantorvabanque.pl --- ')


input()

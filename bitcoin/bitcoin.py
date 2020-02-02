#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup
import datetime


date = datetime.datetime.now()


url = requests.get('https://stooq.pl/q/g/?s=btcpln')
soup = BeautifulSoup(url.content, 'html.parser')

price = soup.find_all('b')[3].find(id="aq_btcpln_c0").text
one_week = soup.find_all(id='c1')[7].text
year = soup.find_all(id='c1')[11].text



print()
print(f'Aktualny kurs bitcoina z dnia {date.strftime("%d/%m/%Y")} z godziny {date.strftime("%H:%M")} wynosi {price} zł')
print()
print(f'Tygodniowa stopa zwrotu waloru wynosi: {one_week}')
print()
print((f'Roczna stopa zwrotu waloru wynosi: {year}'))
print()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime

date = datetime.datetime.now()

url = requests.get('http://www.kantorvabanque.pl/')

soup = BeautifulSoup(url.content, 'html.parser')
# print(soup.prettify()) wyświetli całą stronę html



exchange = soup.find('tbody').get_text() 
# soup.select('tr:nth-child(4) td:nth-child(3)') ukaże cenę kupna funta ale z atrybutami html <td></td>
print()
print()
print(f'Kursy walut ze strony internetowej: http://www.kantorvabanque.pl/ z dnia {date.strftime("%d/%m/%Y")} z godziny {date.strftime("%H:%M")}')
print(exchange)

#tworzenie pliku file.txt i zapisanie w nim kursów walut wraz z opisem i datą
output = open('file.txt','w')
output.write(f'Kursy walut ze strony internetowej: http://www.kantorvabanque.pl/ z dnia {date.strftime("%d/%m/%Y")} z godziny {date.strftime("%H:%M")} {exchange}')
output.close()

input()

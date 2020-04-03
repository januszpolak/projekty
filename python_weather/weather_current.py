#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
import json

#Check IP address
my_ip = requests.get('http://api.ipify.org/').text

#Get current position based on IP address
url1 = 'http://ip-api.com/json/{}'.format(my_ip)
res1 = requests.get(url1)
data = res1.json()


city = data['city']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=a051e71017506e78401e478e6128563d&units=metric'.format(
    city)

res = requests.get(url)
data = res.json()

temp = data['main']['temp']
feels = data['main']['feels_like']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
lon = data['coord']['lon']
lat = data['coord']['lat']
x = time.localtime(sunrise)
y = time.localtime(sunset)

temperatura = f'Temperatura w mieście {city} wynosi {temp} stopni Celciusa'
odczuwalna = f'Temperatura odczuwalna to {feels} stopni Celciusa'
cisnienie = f'Ciśnienie w mieście {city} wynosi {pressure} hPa'
wilgotnosc = f'Wilgotność wynosi {humidity} %'
wschod = f'Wschód słońca o godzienie {x.tm_hour}:{x.tm_min}'
zachod = f'Zachód słońca o godzienie {y.tm_hour}:{y.tm_min}'

print()
print(temperatura)
print()
print(odczuwalna)
print()
print(cisnienie)
print()
print(wilgotnosc)
print()
print(wschod)
print()
print(zachod)
print()
input()

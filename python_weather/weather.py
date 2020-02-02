#!/usr/bin/env python3

import requests
from pprint import pprint
import time
import folium
import webbrowser

city = input('Podaj nazwe miasta:')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=a051e71017506e78401e478e6128563d&units=metric'.format(
    city)

res = requests.get(url)
data = res.json()

# print(res) -- wypisuje status połączenia (200 wszystko ok)

# pprint(data) -- pprint wypisuje nam wartości w json
temp = data['main']['temp']
feels = data['main']['feels_like']
pressure = data['main']['pressure']
humidity = data['main']['humidity']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
lon = data['coord']['lon']
lat = data['coord']['lat']
x = time.gmtime(sunrise)
y = time.gmtime(sunset)


# f to format dzięki czemu można wstzykiwać zmienne do stringów
temperatura = f'Temperatura w mieście {city} wynosi {temp} stopni Celciusa'
odczuwalna = f'Temperatura odczuwalna to {feels} stopni Celciusa'
cisnienie = f'Ciśnienie w mieście {city} wynosi {pressure} hPa'
wilgotnosc = f'Wilgotność wynosi {humidity} %'
wschod = f'Wschód słońca o godzienie {x.tm_hour}:{x.tm_min}'
zachod = f'Zachód słońca o godzienie {y.tm_hour}:{y.tm_min}'

map = folium.Map(location=[lat, lon], zoom_start=13)
folium.Marker([lat, lon], popup=city).add_to(map)


map.save('map.html')
webbrowser.open('map.html')

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

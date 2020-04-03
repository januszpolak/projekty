#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import folium
import webbrowser

#Check IP address
my_ip = requests.get('http://api.ipify.org/').text

#Get current position based on IP address
url = 'http://ip-api.com/json/{}'.format(my_ip)
res = requests.get(url)
data = res.json()

#Get lon and lat and show on map
lat = data['lat']
lon = data['lon']

tileset = 'openstreetmap'
map = folium.Map(location=[lat, lon], tiles = tileset, attr='My Data Attribution', zoom_start=13)
map.save('map.html')
webbrowser.open('map.html')

print(data['country'])
print(data['city'])
print(data['isp'])
print(data['org'])
print(data['query'])



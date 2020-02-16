import requests
import os
import webbrowser
from googletrans import Translator
from urllib.request import urlretrieve


url = 'https://api.nasa.gov/planetary/apod?api_key=D5eW7d8pzrELRM0UxNJl8diqhHYVkc98YoMalk6M'

res = requests.get(url)
data = res.json()
picture = data['url']

#open picture in browser and save it to local directory
webbrowser.open(picture)
filename = picture.strip().split('/')[-1]
urlretrieve(picture.strip(), filename)

#os.system("gsettings set org.gnome.desktop.background picture-uri " + picture)

print(data['date'])
print()
print(data['explanation'])
print('\n\n')


#translate description from english to polish

translator = Translator()
translated_sentence = translator.translate(data['explanation'], src='en', dest='pl')

print(translated_sentence.text)

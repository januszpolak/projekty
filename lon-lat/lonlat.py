import folium
import webbrowser
import keyboard


def start():

    lat = input('Podaj szerokość geograficzną: ')
    lon = input('Podaj długość geograficzną: ')

    map = folium.Map(location=[lat, lon], zoom_start=13)

    map.save('map.html')
    webbrowser.open_new('map.html')


while True:
    start()
    restart = input('Wpisz tak, aby wczytać program ponownie ... ')
    if restart != 'tak':
        print('spadaj')

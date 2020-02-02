import folium
import webbrowser

map = folium.Map(location=[50.049683, 19.944544], zoom_start=13)

map.save('map.html')
webbrowser.open('map.html')

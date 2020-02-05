import random, os
path = '/home/jpolak/Obrazy/Wallpapers/'


random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])


print(random_filename)
os.system("gsettings set org.gnome.desktop.background picture-uri file://" +os.path.join(path,random_filename))
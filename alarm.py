import datetime
import pyglet
alarmHour = int(input("What time do you want to wake up?"))
alarmMinute = int(input("What minut do you want t wake up?"))

while True:
    if(alarmHour == datetime.datetime.now().hour and
       alarmMinute == datetime.datetime.now().minute):
        print("wake up")
	print("to cancel press CTRL+C")
        music = pyglet.resource.media('bomb.wav', streaming=False)
        music.play()
        pyglet.app.run()
        
        break

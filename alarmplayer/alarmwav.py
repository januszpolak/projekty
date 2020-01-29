import datetime


alarmHour = int(input("What time do you want to wake up?"))
alarmMinute = int(input("What minut do you want t wake up?"))

while True:
    if(alarmHour == datetime.datetime.now().hour and
       alarmMinute == datetime.datetime.now().minute):
       

       
    break

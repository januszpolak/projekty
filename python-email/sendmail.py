import smtplib


fromaddr = 'janojp@gmail.com'
toaddr = 'janojp@gmail.com'
password = input('Wprowadź hasło do swojego konta gmail ... ')
message = 'email wyslany przy pomocy pythona'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, password)
server.sendmail(fromaddr,toaddr,message)
server.quit()
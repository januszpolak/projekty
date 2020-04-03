#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib


fromaddr = 'janojp@gmail.com'
toaddr = 'bigj@poczta.fm'
password = input('Wprowadź hasło do swojego konta gmail ... ')
message = 'email wyslany przy pomocy pythona'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, password)
server.sendmail(fromaddr,toaddr,message)
server.quit()

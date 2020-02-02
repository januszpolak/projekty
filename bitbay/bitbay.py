from bs4 import BeautifulSoup
from selenium import webdriver
import requests


driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get = ('https://bitbay.net/pl/kurs-walut/kurs-bitcoin-pln')
res = driver.execute_script('return document.documentElement.outerHTML')
driver.quit()

soup = BeautifulSoup(res, 'lxml')
price = soup.find('div', {'class': 'exchange-wrapper'})

print(price)

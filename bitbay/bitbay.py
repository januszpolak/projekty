import csv
import datetime
from selenium import webdriver


browser = webdriver.Chrome(executable_path=r'./chromedriver')
browser.get('https://bitbay.net/pl/kurs-walut/kurs-bitcoin-pln')

element = browser.find_element_by_xpath(
    '/html/body/main/div[1]/div/div[2]/div/div[1]/div/div/div[2]/p/span').text
element1 = browser.find_element_by_xpath(
    '/html/body/main/div[1]/div/div[2]/div/div[2]/div/div[1]/div/span').text
element2 = browser.find_element_by_xpath(
    '/html/body/main/div[1]/div/div[2]/div/div[2]/div/div[3]/div/span').text
print()
print(f'Średni kurs 1 BTC wynosi {element} zł')
print(f'Cena skupu 1 BTC wynosi {element1} zł')
print(f'Cena sprzedaży 1 BTC wynosi {element2} zł\n')
print('--- Żródło: bitbay.net ---\n')


browser.quit()

e = element.replace(',','')
e1 = e.replace('.',',')

date = datetime.datetime.now()

with open('bitbay.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([date.strftime("%d/%m/%Y"), date.strftime("%H:%M"), e1])

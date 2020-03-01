from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")


browser = webdriver.Chrome(executable_path=r'./chromedriver', options=options)
browser.get('https://airly.eu/map/pl/#50.04374,19.96659,i9576')


place = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]').text
pm10 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div[1]/div/div/div/div[1]/div[1]/div[3]/div[1]').text
pm25 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/strong').text
pm1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div/strong').text
proc1 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/strong').text 
proc2 = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[1]/strong').text
desc = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div[1]/div/div/div/div[1]/div[1]/small').text

print(f'\nAktualna jakość powietrza w Krakowie ul.{place} :\n')
print(f'Pyły PM10 -- {pm10} ug/m3 co daje {proc1} % normy dobowej')
print(f'Pyły PM2.5 -- {pm25} ug/m3 co daje {proc2} % normy dobowej')
print(f'Pyły PM1 -- {pm1} ug/m3')
print(desc)

print('\nPM10 to zanieczyszczenia powietrza o średnicy 10 mikrometrów (jedna tysięczna milimetra) lub mniej.\nNorma WHO (dobowa): 50 µg/m³\n')
print('PM2.5 to zanieczyszczenia powietrza o średnicy 2,5 mikrometra (jedna tysięczna milimetra) lub mniej.\nNorma WHO (dobowa): 25 µg/m³\n')
print('PM1 to zanieczyszczenia powietrza o średnicy 1 mikrometr (jedna tysięczna milimetra) lub mniej.\nNorma WHO: Dla PM1 nie jest zdefiniowana')

browser.quit()

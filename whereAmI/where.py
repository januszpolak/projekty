import pygeoip
import requests


my_ip = requests.get('http://api.ipify.org/').text

gip = pygeoip.GeoIP('GeoIP.dat')
res = gip.record_by_addr(my_ip)

print(res)

from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=2292caf2ed6c00c89402a12881f42fa0')
pprint(r.json)
#london in http is location of area to collect weather data from

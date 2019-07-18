import pyowm


owm =pyowm.owm('{API-KEY}')
observation = owm.weather_at_place('London')
w = observation.get_weather()

w.get_wind()
w.get_humidity()

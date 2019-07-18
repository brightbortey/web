import pyowm

owm=pyowm.OWM('2292caf2ed6c00c89402a12881f42fa0')
observation = owm.weather_at_place('Northern,Ghana')
w = observation.get_weather()


#a=w.get_wind()
#b=w.get_humidity()
#print(a)
#print(b)
print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature())

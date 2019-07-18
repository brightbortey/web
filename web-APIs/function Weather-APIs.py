import pyowm


def weather():
	place = input("Enter location: ")
	
	
	owm = pyowm.OWM('2292caf2ed6c00c89402a12881f42fa0')
	observation = owm.weather_at_place(place)
	w = observation.get_weather()
 
	print(w.get_wind())
	print(w.get_humidity())
	print(w.get_temperature())
	print(w.get_pressure())
weather()

import pyowm

owm = pyowm.OWM('17771e924f711f7021c7f42039d2103e')

place = input("Город: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

print(w)
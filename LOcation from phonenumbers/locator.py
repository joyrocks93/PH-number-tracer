import tkinter

root=tk
import phonenumbers
from test import number
from phonenumbers import geocoder
import folium

target=phonenumbers.parse(number)
location=geocoder.description_for_number(target,"en")
print(location)

from phonenumbers import carrier
service_p=phonenumbers.parse(number)
print(carrier.name_for_number(service_p,"en"))

from opencage.geocoder import  OpenCageGeocode
key='cf1b5a1c630d4a2cb32c626ffbc8266a'

geocoder=OpenCageGeocode(key)
query=str(location)
results= geocoder.geocode(query)
# print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

map=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(map)

map.save("location.html")
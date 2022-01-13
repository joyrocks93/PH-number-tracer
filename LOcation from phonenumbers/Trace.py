import phonenumbers

from test import number
# find the country location
from phonenumbers import geocoder
ch_num=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_num,"en"))

#find the service provider
from phonenumbers import carrier
sp=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(sp,"en"))


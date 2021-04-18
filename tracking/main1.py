import phonenumbers

from phonenumbers import geocoder

samNumber = phonenumbers.parse("+19162521643")

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

from opencage.geocoder import OpenCageGeocode

key = "2c172ea3e27b40cea25e1ad9bb71f12c"
geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
print(results[0]['geometry']['lat'])
print(results[0]['geometry']['lng'])

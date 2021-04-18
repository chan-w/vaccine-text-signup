from flask.templating import render_template
import phonenumbers

from phonenumbers import geocoder

from opencage.geocoder import OpenCageGeocode

key = "2c172ea3e27b40cea25e1ad9bb71f12c"
geocoder = OpenCageGeocode(key)

def code_number(number):
    samNumber = phonenumbers.parse(number)
    yourLocation = geocoder.description_for_number(samNumber, "en")
    return yourLocation

def location_lat_long(yourLocation):
    query = str(yourLocation)

    results = geocoder.geocode(query)
    # print(results[0]['geometry']['lat'])
    # print(results[0]['geometry']['lng'])
    coord = [results[0]['geometry']['lat'], results[0]['geometry']['lng']]
    return coord

if __name__ == '__main__':
    loc = code_number("+12065550100")
    print(str(loc))

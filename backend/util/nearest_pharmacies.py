
api_key = "AIzaSyAedPSTmyoW1ejPtwG_cSu7fEjLxOOUrXg"
# Uses the Geocode API
import requests
from urllib.parse import urlencode

def extract_lat_lng(address_or_postalcode, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"), latlng.get("lng")


def get_nearest_pharmacies(address, number_results=3):
    lat, lng = extract_lat_lng(address)


    places_endpoint_2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params_2 = {
        "key": api_key,
        "location": f"{lat},{lng}",
        "radius": "1500",
        "keyword": "pharmacy"
    }
    params_2_encoded = urlencode(params_2)
    places_url=f"{places_endpoint_2}?{params_2_encoded}"

    r2 = requests.get(places_url)

    ret = []
    for i in range(number_results):
        try:
            result = r2.json()['results'][i]
            ret.append({"name": result.get('name'), "vicinity": result.get('vicinity')})
        except:
            pass
    
    return ret
        
    # Returns the first 3 closest locations and stores it in variables within a 1500 meter radius
    # try:
    #     nameVicinity0 = r2.json()['results'][0]
    #     nameVicinity0.get('name')
    #     vicinity0 = nameVicinity0.get('vicinity')
    # except:
    #     pass

    # try:
    #     nameVicinity1 = r2.json()['results'][1]
    #     name1 = nameVicinity1.get('name')
    #     vicinity1 = nameVicinity1.get('vicinity')
    # except:
    #     pass

    # try:
    #     nameVicinity2 = r2.json()['results'][2]
    #     name2 = nameVicinity2.get('name')
    #     vicinity2 = nameVicinity2.get('vicinity')
    # except:
    #     pass

if __name__ == '__main__':
    print(get_nearest_pharmacies("1600 Amphitheatre Parkway, Mountain View, CA"))

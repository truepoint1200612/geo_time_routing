import os
import requests

BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='
API_KEY = os.environ['GOOGLE_MAP_API_KEY']

def getLatLng(place):
    response = requests.get(BASE_URL+str(place)+'&key='+API_KEY)
    res_json = response.json()
    lat = res_json['results'][0]['geometry']['location']['lat']
    lng = res_json['results'][0]['geometry']['location']['lng']

    return {'lat':lat, 'lng':lng}

if __name__=="__main__":
    place = '首都大学東京日野キャンパス'
    print(getLatLng(place))

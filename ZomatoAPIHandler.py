#import httplib, urllib, urllib2, json
import urllib2
import ast
from Restaurant import Restaurant


def nearbyRestaurants():
    global request_headers
    
    url = 'https://developers.zomato.com/api/v2.1/search?q=qatar&lat=25.3106&lon=51.4460&radius=1000'
    request = urllib2.Request(url, headers=request_headers)
    response = urllib2.urlopen(request).read()
    response = ast.literal_eval(response)
    Rest = response['restaurants']
    RestDict = {}
    j = 1
    for i in Rest:
        RestDict[j] = i
        RestDict[j] = RestDict[j]['restaurant']
        j = j + 1
    return RestDict


def createRestaurant(restaurant):
    global request_headers

    
    name = restaurant.get('name', 'Not Available')
    thumbnail = restaurant.get('thumb', 'CookingLife/NotAvailable.jpg')
    if thumbnail == '':
        thumbnail = 'CookingLife/NotAvailable.jpg'
    location = restaurant['location']
    lon = location.get('longitude', 'Not Available')
    lat = location.get('latitude', 'Not Available')
    phoneNum = restaurant.get('phone_number', 'Not Available')
    address = location.get('address' , 'Not Available')
    pageURL = restaurant.get('url', 'Not Available')
    
    return Restaurant(name, thumbnail, address , phoneNum, lon, lat, pageURL)
    
    
    




request_headers = {
'Accept': 'application/json',
"user-key" : "57b82dac515cf9f504386b85bede46ec"
}

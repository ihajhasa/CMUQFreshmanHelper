#import httplib, urllib, urllib2, json
import urllib2
import ast


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


def createThumbnail(restaurant):
    name = restaurant['name']
    restID = restaurant['id']
    thumbnail = restaurant['thumb']
    location = restaurant['location']
    lon = location['longitude']
    lat = location['latitude']
    return Restaurant(name, thumbnail, 'wegeufiwg', 'regber', lon, lat)
    
    
    




request_headers = {
'Accept': 'application/json',
"user-key" : "57b82dac515cf9f504386b85bede46ec"
}

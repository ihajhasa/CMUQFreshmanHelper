#import httplib, urllib, urllib2, json
import urllib2
import ast
from Restaurant import Restaurant

def search(url):
    global request_headers


    try:
        request = urllib2.Request(url, headers=request_headers)
    except urllib2.HTTPError:
        print 'There was an error with the request'
    response = urllib2.urlopen(request).read()
    response = ast.literal_eval(response)
    response = response['restaurants']
    RestDict = {}
    j = 1
    for i in response:
        RestDict[j] = i['restaurant']
        j = j + 1
    return RestDict
    
    

def getCategories():
    global request_headers
    
    url = 'https://developers.zomato.com/api/v2.1/categories'
    request = urllib2.Request(url, headers=request_headers)
    response = urllib2.urlopen(request).read()
    response = ast.literal_eval(response)
    response = response['categories']
    categories = []
    for i in response:
        categories += [i['categories']]
    return categories
    


def nearbyRestaurants():
    global request_headers
    
    url = 'https://developers.zomato.com/api/v2.1/search?q=qatar&lat=25.3106&lon=51.4460&radius=3000'
    return search(url)


def createRestaurant(restaurant):
    global request_headers

    
    name = restaurant.get('name', 'Not Available')
    thumbnail = restaurant.get('thumb', 'CookingLife/NotAvailable.jpg')
    if thumbnail == '':
        thumbnail = 'CookingLife/NotAvailable.jpg'
    location = restaurant['location']
    lon = location.get('longitude', 'Not Available')
    lat = location.get('latitude', 'Not Available')
    phoneNum = restaurant.get('phone_numbers', 'Not Available')
    if type(phoneNum) == type([]):
        phoneNum = phoneNum[0]
    address = location.get('address' , 'Not Available')
    pageURL = restaurant.get('url', 'Not Available')
    
    return Restaurant(name, thumbnail, address , phoneNum, lon, lat, pageURL)
    
    
    




request_headers = {
'Accept': 'application/json',
"user-key" : "57b82dac515cf9f504386b85bede46ec"
}

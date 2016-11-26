#import httplib, urllib, urllib2, json
import urllib2
import ast
from Restaurant import Restaurant

#Utilizes the search function in Zomato
def search(url):
    global request_headers


    try: #Send request to zomate
        request = urllib2.Request(url, headers=request_headers)
    except urllib2.HTTPError:
        print 'There was an error with the request'

    #Adjust the response to its appropriate type, and filter out any unneccesry data
    response = urllib2.urlopen(request).read()
    response = ast.literal_eval(response)
    response = response['restaurants']

    #This is a dictionary that will contain all the restaurants from the response
    RestDict = {}
    #Dynamically generated keys to adjust to different sized responses
    j = 1
    for i in response:
        #Copy over all the restaurants
        RestDict[j] = i['restaurant']
        j = j + 1
    #Retaurn the restaurant dictionary
    return RestDict
    
    
#Gets the categories zomato has for its restaurants
def getCategories():
    global request_headers

    #Send Request and get response    
    url = 'https://developers.zomato.com/api/v2.1/categories'
    request = urllib2.Request(url, headers=request_headers)
    response = urllib2.urlopen(request).read()

    #Adjust response to its appropiate format
    response = ast.literal_eval(response)
    response = response['categories']

    #List will ocntain all the categoires
    categories = []
    for i in response:
        #Add the categories to the categories list
        categories += [i['categories']]
    #Return the results
    return categories
    

#get nearbyRestaurants (pre-fixed to the male dorms)
def nearbyRestaurants():
    global request_headers
    
    url = 'https://developers.zomato.com/api/v2.1/search?q=qatar&lat=25.3106&lon=51.4460&radius=3000'
    return search(url)

#Extracts all the necessary info from the dictionary to be able to make the restaurant object
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
    #Return the object
    return Restaurant(name, thumbnail, address , phoneNum, lon, lat, pageURL)
    
    
    



#The headers needed by Zomato in order for me to recieve a response
request_headers = {
'Accept': 'application/json',
"user-key" : "57b82dac515cf9f504386b85bede46ec"
}

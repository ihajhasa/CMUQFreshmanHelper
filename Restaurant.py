from Tkinter import *
from PIL import Image, ImageTk
import urllib
import os
import Tkinter as TK
import webbrowser

from math import radians, cos, sin, asin, sqrt

#http://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-
#between-two-latitude-longitude-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km


class Restaurant:

    def __init__(self, name, thumbnail, address, phoneNum, lon, lat, url):
        self.name = name
        self.thumbnail = thumbnail.replace('\\','')
        if self.thumbnail != 'CookingLife/NotAvailable.jpg':
            imageName = self.thumbnail.split('/')
            imageName = imageName[-1]
            self.image = urllib.urlretrieve(self.thumbnail, imageName)
            self.thumbnail = imageName
        self.image = ''
        self.address = address
        #After the 25th Character, it will find the next comma, then add a \n to make the address more compact
        if address != 'Not Available' and len(address) > 25:
            i = 20
            while i < len(self.address):
                if self.address[i] == ',':
                    self.address = self.address[:i+1] + '\n' + self.address[i+1:]
                    i = i + 17
                i = i + 1
            
                
        self.phoneNum = phoneNum
        self.longitude = lon
        self.latitude = lat
        self.URL = url.replace('\\', "")

        self.frame = ''
        self.label1 = ''
        self.label2 = ''
        

    def getName(self):
        return self.name
    def getThumbnail(self):
        return self.thumbnail
    def getPhoneNum(self):
        return self.phoneNum
    def getLocation(self):
        return (self.longitude, self.latitude)
    def getAddress(self):
        return self.address

    def __str__(self):
        distance = haversine(51.446, 25.3106, float(self.longitude), float(self.latitude))
        return self.name + '\n' +  self.address + '\n' +  self.phoneNum + '\n' + "Distance: " + str(distance)[:4] + 'km'

    def t(e, link):
        webbrowser.open_new_tab(link)

    def makeThumbnail(self, window):
        self.frame = TK.Frame(window)
        self.frame.config(width = 10000, height = 10000)
        self.frame.config(bd = 10, relief = GROOVE)
        self.label1 = TK.Label(self.frame)


        image = Image.open(self.thumbnail)
        image = ImageTk.PhotoImage(image.resize((200,200), Image.ANTIALIAS))
        self.image = image


        self.label1.config(image = self.image)
        
        
        self.label2 = TK.Label(self.frame, text = self.__str__())

        self.label1.pack()
        self.label2.pack()

        
        
        

    

from Tkinter import *
from PIL import Image, ImageTk
import urllib
import os
import Tkinter as TK
import webbrowser


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
            i = 25
            while i < len(self.address) and self.address[i] != ',':
                i = i + 1
            if i+1 != len(self.address):
                self.address = self.address[:i+1] + '\n' + self.address[i+1:]
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
        return self.name + '\n' +  self.address + '\n' +  self.phoneNum + '\n' +  self.longitude+ '\n' +  self.latitude

    def t(e, link):
        print link
        webbrowser.open_new_tab(link)

    def makeThumbnail(self, window):
        print self.thumbnail, self.name, self.URL
        self.frame = TK.Frame(window)
        self.frame.config(bd = 10, highlightbackground='blue')
        self.label1 = TK.Label(self.frame)


        image = Image.open(self.thumbnail)
        image = ImageTk.PhotoImage(image.resize((200,200), Image.ANTIALIAS))
        self.image = image


        self.label1.config(image = self.image)
        
        
        self.label2 = TK.Label(self.frame, text = self.__str__())

        self.label1.pack()
        self.label2.pack()
        
        
        
        

    

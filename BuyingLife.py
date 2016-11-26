import getCarrefourPromotions
from Tkinter import *
from PIL import Image, ImageTk
import urllib2
import os
import webbrowser

#Display the pdf file containing the HyperMarket Deals
def getHMPro():
    #Retrieve the real path to this python file 
    url = os.path.realpath('BuyingLife.py')

    #Remove 'BuyingLife.py' from the path
    url = url.split('/')
    url = url[:len(url) -1]

    #Add Folder Carrefour_Lulu followed by pdf file name
    url = url + ['Carrefour_Lulu'] + ['carrefourHMPromotions.pdf']

    #Merje togther the path, add the file:// protocol, so it knows it is a file not a web page
    url = 'file://' + '/'.join(url)

    #Since it is a file protocol, it will know to open it using preview, and not the web browser
    #Or a web browser that can handle pdf files
    webbrowser.open_new_tab(url)

#Display the pdf file containing the deals from the SuperMarket Carrefour
def getSMPro():
    
    #Adjust path to that of the pdf file (similar steps to above)
    url = os.path.realpath('BuyingLife.py')
    url = url.split('/')
    url = url[:len(url) -1]
    url = url + ['Carrefour_Lulu'] + ['carrefourSMPromotions.pdf']

    #Adjust the link to the correct format with correct protocol
    url = 'file://' + '/'.join(url)

    #Retrieves file
    webbrowser.open_new_tab(url)



#This will contain all the elements of the frame of the program
class BuyingLife:

    def __init__(self, mainWnd):
        #Retrieve the latest deals from carrefours website
        #Executed only the first time Buying Life is called
        getCarrefourPromotions.getPromotionBooklet()

        #Adjust main window to certain size
        mainWnd.geometry('1325x890')
        mainWnd.config(bg = 'white')

        #Frame that will contain everything (will contain a canvas)
        self.frame = Frame(mainWnd)
        self.frame.config(width = 1500, height = 1000, bg = 'white')


        
        #This canvas will encapsulate all the elements of the program
        self.canvas = Canvas(self.frame, bg = 'white')
        self.canvas.config(width = 1500, height = 855)

        #Create photoImage of the background and adjust the size
        self.wallpaper = Image.open('Carrefour_Lulu/carrefour.jpg')
        self.wallpaper = ImageTk.PhotoImage(self.wallpaper.resize((1300,855), Image.ANTIALIAS))
        
        #Label that will display the image, and everything will be gridded over the label
        self.label = Label(self.canvas, image = self.wallpaper)


        #Create a photoimage of the HyperMarket Icon and SuperMarket Icon for the buttons
        self.HMPromoIcon = ImageTk.PhotoImage(Image.open('Carrefour_Lulu/HMPromoIcon.jpg'))
        self.SMPromoIcon = ImageTk.PhotoImage(Image.open('Carrefour_Lulu/SMPromoIcon.jpg'))

        #Buttons, when clicked will open the relative pdf file
        displayHMPBtn = Button(self.canvas,
                               text = ' Get HyperMarket Promotions',
                               command = getHMPro, height = 7,
                               image = self.HMPromoIcon)
        displaySMPBtn = Button(self.canvas,
                               text = '\n\n\nGet SuperMarket Promotions\n\n\n',
                               command = getSMPro, height = 7,
                               image = self.SMPromoIcon)
        displaySMPBtn.config(width = 200, height = 250)
        displayHMPBtn.config(width = 200, height = 250)
        
        #Grid Label first, so anything that overlaps will be displayed above the label and visible to the user
        self.label.grid(row = 0, rowspan = 6, column = 0, columnspan = 5)
        displayHMPBtn.grid(row = 2, column = 1)
        displaySMPBtn.grid(row = 2, column = 3)

        #Pack the canvas into the frame
        self.canvas.pack()
        
        

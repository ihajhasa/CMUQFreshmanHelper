import os
import webbrowser
from Tkinter import *
from PIL import Image, ImageTk

class CleaningProgram:

    def __init__(self, dormFrame):

        #Retieves absolute location of claender and displays it
        def displayLargerImage(e):
            if (e.x >= 16 and e.y>= 133) and (e.x <= 139 and e.y <=293):
                #Get path to the image
                url = os.path.realpath('CleaningProgram.py')
                url = url.split('/')
                url = url[:len(url) - 1]
                url += ['Cleaning'] + ['Cleaning_List.jpg']
                url = '/'.join(url)
                url = 'file://' + url
                
                webbrowser.open_new_tab(url)

        #Cretaes a new tab to go to wikiHow's page
        def goToWikiHowCleaning():
            url = 'http://www.wikihow.com/Clean-Your-Room'
            webbrowser.open_new_tab(url)

        #Cretaes a new tab to go to about housecleaning's page
        def goToAHK():
            url = 'http://housekeeping.about.com/od/roombyroomguide/ht/intensedorm.htm'
            webbrowser.open_new_tab(url)


        #Establish all widgets
        
        self.frame = Frame(dormFrame)

        self.displayImage = ImageTk.PhotoImage(Image.open('Cleaning/DisplayTips.jpg'))
        self.LabelImage = Label(self.frame, image = self.displayImage)
        self.LabelImage.bind('<Button-1>', displayLargerImage)

        self.splitFrame = Frame(self.frame, height = 70)

        self.WHL = ImageTk.PhotoImage(Image.open('Cleaning/WikiHowLogo.jpg'))
        self.link1 = Button(self.frame, image = self.WHL, command = goToWikiHowCleaning)

        self.AHK = ImageTk.PhotoImage(Image.open('Cleaning/AboutHK.jpg'))
        self.link2 = Button(self.frame, image = self.AHK, command = goToAHK)

        
        #Everything is displayed, except for the frame itself
        self.LabelImage.grid(row = 0, rowspan = 3, column = 0, columnspan = 2)
        self.splitFrame.grid(row = 1, column = 2)
        self.link1.grid(row = 0, column = 2)
        self.link2.grid(row = 2, column = 2)
        

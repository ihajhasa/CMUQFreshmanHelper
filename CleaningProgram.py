import os
import webbrowser
from Tkinter import *
from PIL import Image, ImageTk

#Images and links are taken from the wikihow.com and about.com


class CleaningProgram:
    #The program cleaning program
    def __init__(self, dormFrame):

        def displayLargerImage(e):
            #If true, then user clicked on the 'enlarge schedule button'
            if (e.x >= 16 and e.y>= 133) and (e.x <= 139 and e.y <=293):
                #Get path to the image

                #Get relative path to this .pyfile
                url = os.path.realpath('CleaningProgram.py')
                
                url = url.split('/')
                      
                #Remove the cleaningProgram.py file from the path
                url = url[:len(url) - 1]
                #Add the cleaning folder and the image within it
                url += ['Cleaning'] + ['Cleaning_List.jpg']
                url = '/'.join(url)

                #Create full url with appropriate protocols
                url = 'file://' + url

                #Open the image
                webbrowser.open_new_tab(url)

        #Opens new tab to the wikihow page
        def goToWikiHowCleaning():
            url = 'http://www.wikihow.com/Clean-Your-Room'
            webbrowser.open_new_tab(url)

        #Opens the about.com page in a new tab
        def goToAHK():
            url = 'http://housekeeping.about.com/od/roombyroomguide/ht/intensedorm.htm'
            webbrowser.open_new_tab(url)

        
        #main frame
        self.frame = Frame(dormFrame)

        #Create photoimage of the tips image
        self.displayImage = ImageTk.PhotoImage(Image.open('Cleaning/DisplayTips.jpg'))
        #Create a label to display the image
        self.LabelImage = Label(self.frame, image = self.displayImage)
        #Check where the user clicks in the label
        self.LabelImage.bind('<Button-1>', displayLargerImage)

        #spacing frame
        self.splitFrame = Frame(self.frame, height = 70)

        #Create the photoimge of both icons for the two helpful websites
        self.WHL = ImageTk.PhotoImage(Image.open('Cleaning/WikiHowLogo.jpg'))
        self.link1 = Button(self.frame, image = self.WHL, command = goToWikiHowCleaning)

        self.AHK = ImageTk.PhotoImage(Image.open('Cleaning/AboutHK.jpg'))
        self.link2 = Button(self.frame, image = self.AHK, command = goToAHK)

        
        #Display all the elements
        self.LabelImage.grid(row = 0, rowspan = 3, column = 0, columnspan = 2)
        self.splitFrame.grid(row = 1, column = 2)
        self.link1.grid(row = 0, column = 2)
        self.link2.grid(row = 2, column = 2)

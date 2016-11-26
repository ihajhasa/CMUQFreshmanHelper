from Tkinter import *
from PIL import Image, ImageTk
import webbrowser

#Function that opens a new tab in browser, and takes you to the youtube page
def youTubeLaundry():
        #The fact youtube relies on a search query, means that the link will continiously update with the increase of more and better content regarding the search term I used
    url = 'https://www.youtube.com/results?search_query=how+to+do+laundry'
    webbrowser.open_new_tab(url)

def goToYouTube(e):
    if e.x >= 548 and e.x <= 848: #User clicked in the section of the image containing the Youtube logo
        if e.y >= 648 and e.y <= 906:
            youTubeLaundry()

class LaundryProgram:
        
    def __init__(self, dormFrame):
        
        #Create the widgets
        self.frame = Frame(dormFrame)
        
        self.helpSheet= ImageTk.PhotoImage(Image.open('LaundrySymbolSheetImages/HelpSheetSymbol-1.jpg').resize((900,930), Image.ANTIALIAS))
        self.labelForImage = Label(self.frame, image = self.helpSheet)
        self.labelForImage.bind('<Button-1>', goToYouTube)

        self.splitFrame = Frame(self.frame)
        self.splitFrame.config(width = 75)
            
        #Everything is displayed, except for the frame itself
        self.labelForImage.grid(row = 0, rowspan = 5, column = 0, columnspan = 7)
        self.splitFrame.grid(row = 0, column = 7)

        

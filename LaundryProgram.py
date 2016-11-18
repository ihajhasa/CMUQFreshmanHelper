from Tkinter import *
from PIL import Image, ImageTk
import webbrowser

#Function that opens a new tab in browser, and takes you to the youtube page
def youTubeLaundry():
        #The fact youtube relies on a search query, means that the link will continiously update with the increase of more and better content regarding the search term I used
    url = 'https://www.youtube.com/results?search_query=how+to+do+laundry'
    webbrowser.open_new_tab(url)

class LaundryProgram:
        
    def __init__(self, dormFrame):
        
        #Create the widgets
        self.frame = Frame(dormFrame)
        
        self.helpSheet= ImageTk.PhotoImage(Image.open('LaundrySymbolSheetImages/HelpSheetSymbol.jpg'))
        self.labelForImage = Label(self.frame, image = self.helpSheet)

        self.splitFrame = Frame(self.frame)
        self.splitFrame.config(width = 75)
            
        self.YouTubeIcon = ImageTk.PhotoImage(Image.open('IconImages/YouTubeIconLaundry.jpg'))
        self.youTubeLaundryBtn = Button(self.frame)
        self.youTubeLaundryBtn.config( image = self.YouTubeIcon, command = youTubeLaundry)

        #Everything is displayed, except for the frame itself
        self.labelForImage.grid(row = 0, rowspan = 5, column = 0, columnspan = 7)
        self.splitFrame.grid(row = 0, column = 7)
        self.youTubeLaundryBtn.grid(row = 0, column = 8)

        

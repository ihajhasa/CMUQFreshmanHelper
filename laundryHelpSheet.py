from Tkinter import *
from PIL import Image, ImageTk
import webbrowser

def youTubeLaundry():
    #The fact youtube relies on a search query, means that the link will continiously update with the increase of more and better content regarding the search term I used
    url = 'https://www.youtube.com/results?search_query=how+to+do+laundry'
    webbrowser.open_new_tab(url)

def displayHelpWindow():
    global avoidGarbageCollect
    
    symbolWnd = Toplevel()
    symbolWnd.geometry('1500x1080')
        
    helpSheet= ImageTk.PhotoImage(Image.open('LaundrySymbolSheetImages/HelpSheetSymbol.jpg'))
    labelForImage = Label(symbolWnd, image = helpSheet)

    splitFrame = Frame(symbolWnd)
    splitFrame.config(width = 200)
        
    YouTubeIcon = ImageTk.PhotoImage(Image.open('IconImages/YouTubeIconLaundry.jpg'))
    youTubeLaundryBtn = Button(symbolWnd)
    youTubeLaundryBtn.config( image = YouTubeIcon, command = youTubeLaundry)
        
    labelForImage.grid(row = 0, rowspan = 5, column = 0, columnspan = 7)
    splitFrame.grid(row = 0, column = 7)
    youTubeLaundryBtn.grid(row = 0, column = 8)

    avoidGarbageCollect += [symbolWnd, helpSheet, YouTubeIcon]


avoidGarbageCollect = []

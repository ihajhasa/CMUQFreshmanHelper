from Tkinter import *
from PIL import Image, ImageTk

def findRoom(e):
    print e.x,e.y

def selectGroundFloor(maps, label):
    label.config(image = maps[0])
            
def selectFirstFloor(maps, label):
    label.config(image = maps[1])

class CMUMap:

        
    def __init__(self, mainWnd):
        #Main Frame
        self.frame = Frame(mainWnd)
        self.frame.config(width = 1250, height = 940)

        #Import Images and Store them
        GFlevel = Image.open('Map/MapFG.jpg')
        GFlevel = ImageTk.PhotoImage(GFlevel.resize((1000,750), Image.ANTIALIAS))
        F1level = Image.open('Map/MapF1.jpg')
        F1level = ImageTk.PhotoImage(F1level.resize((1000,750), Image.ANTIALIAS))
        self.Maps = [GFlevel, F1level]

        #Space Frame(s)
        spaceFrameUpper = Frame(self.frame, height = 40)
        spaceFrameUpper.grid(row = 1,column = 0, columnspan = 3)

        spaceFrameLower = Frame(self.frame, height = 40)
        spaceFrameLower.grid(row = 3,column = 0, columnspan = 3)

        #Width Space Frame
        widthSpaceFrame = Frame(self.frame, width = 200)
        widthSpaceFrame.grid(row = 0, rowspan = 3, column = 0)

        
        #Label that will dislay the map
        self.currentMapDisplayed = Label(self.frame, image = self.Maps[0])
        self.currentMapDisplayed.bind('<Button-1>', findRoom)

        #Create the buttons
        self.selectGF = Button(self.frame, command = lambda maps = self.Maps,
                               label = self.currentMapDisplayed: selectGroundFloor(maps, label),
                               text = "Ground Floor", pady = 10)
        
        self.selectF1 = Button(self.frame, command = lambda maps = self.Maps,
                               label = self.currentMapDisplayed: selectFirstFloor(maps, label),
                               text = "First Floor", pady = 10)

        
        #Display Everything
        self.currentMapDisplayed.grid(row = 2, column = 1, columnspan = 3)
        self.selectGF.grid(row = 0, column = 1)
        self.selectF1.grid(row = 0, column = 3)
        

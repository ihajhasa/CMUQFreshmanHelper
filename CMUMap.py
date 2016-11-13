from Tkinter import *
from PIL import Image, ImageTk

class CMUMap:

    def __init__(self, mainWnd):

        def findRoom(e):
            print e.x,e.y

        def selectGroundFloor(maps, label):
            label.config(image = maps[0])
            
        def selectFirstFloor(maps, label):
            label.config(image = maps[1])
        
            

        
        self.frame = Frame(mainWnd)
        self.frame.config(width = 1250, height = 940)


        GFlevel = ImageTk.PhotoImage(Image.open('Map/MapFG.jpg'))
        F1level = ImageTk.PhotoImage(Image.open('Map/MapF1.jpg'))

        
        self.Maps = [GFlevel, F1level]

        self.currentMapDisplayed = Label(self.frame, image = self.Maps[0])
        self.currentMapDisplayed.bind('<Button-1>', findRoom)

        self.selectGF = Button(self.frame, command = lambda maps = self.Maps,
                               label = self.currentMapDisplayed: selectGroundFloor(maps, label), text = "Ground Floor")
        
        self.selectF1 = Button(self.frame, command = lambda maps = self.Maps,
                               label = self.currentMapDisplayed: selectFirstFloor(maps, label), text = "First Floor")

        

        self.currentMapDisplayed.grid(row = 1, column = 0, columnspan = 2)
        self.selectGF.grid(row = 0, column = 0)
        self.selectF1.grid(row = 0, column = 1)
        

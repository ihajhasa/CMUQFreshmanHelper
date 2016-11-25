from Tkinter import *
from PIL import Image, ImageTk
import time
from threading import Timer

sectionsGF = ['CS Department', '1032 - Computer Cluster', 'Academic Resource Center', 'Food Court',
              'Student Majlis', '1185 - Computer Cluster', 'Library']
sectionsF1 = []


def findRoom(e):
    print e.x,e.y

def drawLine(x, c): #Utilizes the map function
    #Maintains the same properties for all drawn lines
    c.create_line(x[0],x[1],x[2],x[3], fill="red", width = 2)
    #c.tag_raise(line)

def drawCircle(x,c):
    c.create_oval(x[0], x[1], x[2], x[3], fill="red", width = 2)

def drawRectangle(x,c):
    c.create_rectangle(x[0],x[1],x[2],x[3], outline = 'red', width = 2)

def createLinePath(x):
    i = 0
    path = []
    while i < len(x) - 2:
        path = path + [[ x[i],x[i+1], x[i+2], x[i+3] ]]
        i += 2
    path.append([x[-2], x[-1], x[0], x[1]])
    return path
        

def drawShape(current, maps, section, c):
    #c for canvas
    if section in sectionsGF:
        global sectionsGF
        global sectionsF1
        global presentResult

        
        if maps[0] != current[0]:
            selectGroundFloor(maps, c, -1000, current)
            executeDelay = Timer(11, lambda : drawShape(current, maps, section, c))
            executeDelay.start()
        else:
            c.delete('all')
            c.create_image(0,0,image = maps[0], anchor = NW)
            if section == sectionsGF[0]:
                path = [[130,137,130,261],
                      [130,261,210,261],
                      [210,261,234,248],
                      [234,248,234,137],
                      [234,137,130,137]]
                map(lambda x: drawLine(x,c), path)
            elif section == sectionsGF[1]:
                map(lambda x: drawRectangle(x,c), [[346,138,383,185]])
            elif section == sectionsGF[2]:
                map(lambda x: drawRectangle(x,c), [[419,172,516,220]])
            elif section == sectionsGF[3]:
                map(lambda x: drawRectangle(x,c), [[260,381,362,449]])
            elif section == sectionsGF[4]:
                map(lambda x: drawRectangle(x,c), [[383,380,483,440]])
            elif section == sectionsGF[5]:
                path = [405,600,420,654,495,636,479,577]
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            elif section == sectionsGF[6]:
                path = '539 438 689 476 690 512 750 511 751 355 715 353 715 396 676 388 677 328 608 322 610 405 550 392'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)

def selectGroundFloor(maps, c, transition, currentImage):
    c.delete('all')
    c.create_image(transition,0, image = maps[0], anchor = NW)
    c.create_image(transition + 1000, 0, image = maps[1], anchor = NW)
    if transition < 0:
        c.after(100, lambda : selectGroundFloor(maps, c, transition + 10, currentImage))
    else:
        c.delete('all')
        c.create_image(0,0, image = maps[0], anchor = NW)
        del currentImage[0]
        currentImage.append(maps[0])
        
            
def selectFirstFloor(maps, c, transition, currentImage):
    c.delete('all')
    c.create_image(transition,0, image = maps[1], anchor = NW)
    c.create_image(transition - 1000, 0, image = maps[0], anchor = NW)
    if transition > 0:
        c.after(100, lambda : selectFirstFloor(maps, c, transition - 10, currentImage))
    else:
        c.delete('all')
        c.create_image(0,0, image = maps[1], anchor = NW)
        del currentImage[0]
        currentImage.append(maps[1])

class CMUMap:

        
    def __init__(self, mainWnd):
        global sectionsGF, sectionsF1
        
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
        #Canvas for the label to be in

        self.canvas = Canvas(self.frame)
        self.canvas.config(width = 1000, height = 750)
        self.canvas.create_image(0,0, image = self.Maps[0], anchor = NW)
        
    
        self.canvas.bind('<Button-1>', findRoom)

        #Create the buttons

        self.currentDisplayedImage = [self.Maps[0]] #This is a reference to a list, which when changed is updated into the variable
        
        self.selectGF = Button(self.frame, command = lambda maps = self.Maps,
                               c = self.canvas: selectGroundFloor(maps, c, -1000, self.currentDisplayedImage),
                               text = "Ground Floor", pady = 10)
        
        self.selectF1 = Button(self.frame, command = lambda maps = self.Maps,
                               c = self.canvas: selectFirstFloor(maps, c, 1000, self.currentDisplayedImage),
                               text = "First Floor", pady = 10)

        #List of options, and button to execute request
        self.optionsFrame = Frame(self.frame)
        self.optionList = Listbox(self.optionsFrame)
        for section in sectionsGF:
            self.optionList.insert(END, section)
        for section in sectionsF1:
            self.optionList.insert(END, section)

        requestSecBtn = Button(self.optionsFrame, text = 'Request Section',
                               command = lambda : drawShape(self.currentDisplayedImage, self.Maps, self.optionList.get(ACTIVE), self.canvas))
        
        #Display Everything
        self.canvas.grid(row = 2, column = 1, columnspan = 3)
        self.selectGF.grid(row = 0, column = 1)
        self.selectF1.grid(row = 0, column = 3)
        self.optionsFrame.grid(row = 2, column = 0)
        self.optionList.pack()
        requestSecBtn.pack()

        
        

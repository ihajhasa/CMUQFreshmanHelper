from Tkinter import *
from PIL import Image, ImageTk
import time
from threading import Timer

#Global variable of 
sectionsGF = ['CS Department', '1032 - Computer Cluster', 'Academic Resource Center', 'Food Court',
              'Student Majlis', '1185 - Computer Cluster', 'Library', 'Admissions Area', 'Student Affairs',
              '1064 - Lecture Hall', 'Study Rooms - Ground Floor', 'Male prayer Room',
              '1213 - Lecture Hall', '1202 - Lecture Hall']
sectionsF1 = ['Math Department', '2051 - Seminar Room', 'IT Department', 'Rec. Room \\ Student Lounge',
              'Female prayer Room', 'Biology Department', 'Study Rooms - First Floor', 'GYM + Locker Rooms',
              '2163 - Lecture Hall', '2152 - Lecture Hall', 'Info. Systems Department']

buttons = []




#All of these get are utilized by map functions
    #They get a list containing 4 elements which are the coodinates
    #let s = start and e = end, x is x coor and y is y coor
    #The format of the list will be [sx, sy, ex, ey]

def drawLine(x, c): #Utilizes the map function
    
    #Maintains the same properties for all the lines to be drawn
    c.create_line(x[0],x[1],x[2],x[3], fill="red", width = 2)

def drawCircle(x,c):
    #Maintains the same properties for all the circles to be drawn
    c.create_oval(x[0], x[1], x[2], x[3], outline="red", width = 2)

def drawRectangle(x,c):
    #Maintains the same properties for all the rectangles to be drawn
    c.create_rectangle(x[0],x[1],x[2],x[3], outline = 'red', width = 2)

#-------------------------------------------------------------------------------

    
#Creates a list of lists, each of which is the coordinates needed to create a line
def createLinePath(x):
    #x would be a list that would have the coordinates you need to pass through in order
    i = 0
    path = []
    while i < len(x) - 2:
        #Add the start points of the line, and end points of the line
        path = path + [[ x[i],x[i+1], x[i+2], x[i+3] ]]
        #The end points of the previous line are the start of the next, which is why we only skip 2
        i += 2
    #Add the last line, that will connect where we end to where we started, because we are highlighting a box
    path.append([x[-2], x[-1], x[0], x[1]])
    #Return the list of lists
    return path

        
#Draws around the section the user wants to know the location of
def drawShape(current, maps, section, c):
    #c for canvas
    global sectionsGF
    global sectionsF1
    global presentResult

    #If in Ground Floor
    if section in sectionsGF:

        #If true, that means the current map displayed is not where the section is, so we have to switch maps
        if maps[0] != current[0]:
            #Switch the floors
            switchFloor(maps, c, current, 'GF')
            
            #Wait 13 sseconds, which is the amount of time needed for the animation transition to end to re-execute the drawshape function
                #Since we are on the correct map, then there is no need to transition to another map
            executeDelay = Timer(13.2, lambda : drawShape(current, maps, section, c))
            executeDelay.start()
        else:
            #Clear any previously drawn things
            c.delete('all')
            #Redraw the cirrect map, since it would be erased
            c.create_image(0,0,image = maps[0], anchor = NW)

            #What all these if statements do is check which section the user requested from the global list of sections
            #Depending on which if statement is set to be true, then draw the shape using map and
            #the three functions above to draw lines, circles, or/and rectangles
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
            elif section == sectionsGF[7]:
                path = '592 299 630 87 913 87 912 299'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            elif section == sectionsGF[8]:
                path = '635 99 623 159 653 159 653 153 676 152 676 95'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            elif section == sectionsGF[9]:
                map(lambda x: drawRectangle(x,c), [[484,223,542,279]])
            elif section == sectionsGF[10]:
                path = '529 451 514 473 543 491 562 467'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            elif section == sectionsGF[11]:
                map(lambda x: drawCircle(x,c), [[287,229,319,259]])
            elif section == sectionsGF[12]:
                path = '148 433 168 480 120 506 091 458'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            elif section == sectionsGF[13]:
                path = '191 512 238 554 188 594 146 552'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
    elif section in sectionsF1: #This means section in first floor
        #Checks if the current map displayed is the first floor
        if maps[1] != current[0]:
            #If not then switch floors
            switchFloor(maps, c, current, 'F1')
            
            #Re-execute the same drawShape function, but after 13 seconds, which is when the animation finishes
            executeDelay = Timer(13.2, lambda : drawShape(current, maps, section, c))
            executeDelay.start()
        else:
            #Clear any previously drawn shapes
            c.delete('all')
            #Redraw image because it would be erased
            c.create_image(0,0,image = maps[1], anchor = NW)

            #What all these if statements do is check which section the user requested from the global list of sections
            #Depending on which if statement is set to be true, then draw the shape using map and
            #the three functions above to draw lines, circles, or/and rectangles
            if section == sectionsF1[0]:
                path = '145 128 145 270 220 270 244 248 244 128'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            elif section == sectionsF1[1]:
                map(lambda x: drawRectangle(x,c), [[422,179,468,208]])
            elif section == sectionsF1[2]:
                map(lambda x: drawRectangle(x,c), [[659,149,723,236]])
            elif section == sectionsF1[3]:
                map(lambda x: drawRectangle(x,c), [[615,342,739,428]])
            elif section == sectionsF1[4]:
                map(lambda x: drawCircle(x,c), [[291,228,322,261]])
            if section == sectionsF1[5]:
                path = '215 420 219 429 223 442 227 453 233 466 239 473 248 483 257 492 268 502 283 509 269 530 251 524 239 514 228 502 220 492 210 479 203 466 196 450 192 436 190 420'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            elif section == sectionsF1[6]:
                map(lambda x: drawRectangle(x,c), [[394,495,426,519]])
                map(lambda x: drawRectangle(x,c), [[477,383,512,401]])
            if section == sectionsF1[7]:
                path = '216 536 271 580 229 621 199 604 176 576'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            if section == sectionsF1[8]:
                path = '412 601 429 661 500 642 479 584'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            if section == sectionsF1[9]:
                path = '514 568 564 535 597 583 543 613'.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            if section == sectionsF1[10]:
                path = '478 513 489 508 500 500 510 490 522 475 530 463 538 451 547 437 552 424 '
                path = path + '556 411 586 420 579 433 574 448 568 461 556 476 543 495 530 509 521 517 510 529 491 539'
                path = path.split(' ')
                path = createLinePath(path)
                map(lambda x: drawLine(x,c), path)
            
#Disables all buttons, except for the return to main page button
def DisableButtons():
    global buttons
    #For every button in the global variable, disable
    for button in buttons:
        button.config(state=DISABLED)

#Enable all buttons, except for the return to main page button
def EnableButtons():
    global buttons
    #For every button in the global variable, enable
    for button in buttons:
        button.config(state = NORMAL)


#This function will switch between the maps of the 2 CMUQ Campus floors
def switchFloor(maps,c, currentImage, floor):
    
    #Check which floor user wants to go to, and execute only if the current map isnt the same one the user wanted
    if floor == 'GF' and maps[0] != currentImage[0]:
        DisableButtons() #Disable the buttons so the user cannot create another request while the animation occurs
        selectGroundFloor(maps, c, -1000, currentImage)
        #Re enable the buttons after the animations finish
        reEnableBtns = Timer(13, EnableButtons)
        reEnableBtns.start()
    elif floor == 'F1' and maps[1] != currentImage[0]:
        DisableButtons()#Disable the buttons so the user cannot create another request while the animation occurs
        selectFirstFloor(maps, c, 1000, currentImage)
        #Re enable the buttons after the animations finish
        reEnableBtns = Timer(13, EnableButtons)
        reEnableBtns.start()
    
    

    
#Displays the ground floor map
def selectGroundFloor(maps, c, transition, currentImage):
    #Clear canvas
    c.delete('all')
    #draw the ground floor map with offset transition
    c.create_image(transition,0, image = maps[0], anchor = NW)
    #draw the first floor map with offset transition + 1000
    c.create_image(transition + 1000, 0, image = maps[1], anchor = NW)
    
    if transition < 0: #If the top left corner of the ground floor map is not in the canvas
        #Redraw with transition 10 pixels to the right
        c.after(100, lambda : selectGroundFloor(maps, c, transition + 10, currentImage))
    else:
        #We reached the end
        #The top left corner of the map may not be in 0,0 of the canvas,
        #So redraw the map with its top left coordinate on 0,0
        c.delete('all')
        c.create_image(0,0, image = maps[0], anchor = NW)

        #Update CurrentImage to ground floor
        del currentImage[0]
        currentImage.append(maps[0])
        
# Displays the first floor map of the campus, with sick animations          
def selectFirstFloor(maps, c, transition, currentImage):
    c.delete('all')
    #Draw the map of first floor with offset transition, and ground floor map with offset transition - 1000
    c.create_image(transition,0, image = maps[1], anchor = NW)
    c.create_image(transition - 1000, 0, image = maps[0], anchor = NW)
    if transition > 0: ##If the top right corner of the ground floor map is in the canvas
        c.after(100, lambda : selectFirstFloor(maps, c, transition - 10, currentImage))
    else:#That means only the first floor map is visible,
        #The top left corner may not be on the top left corner of the canvas so redraw the map in the appropiate location
        c.delete('all')
        c.create_image(0,0, image = maps[1], anchor = NW)

        #update currentImages to have first floor
        del currentImage[0]
        currentImage.append(maps[1])


class CMUMap:
    #This is the CMU map program
    def __init__(self, mainWnd):
        global sectionsGF, sectionsF1
        global buttons
        
        #Main Frame and adjust it to app requirements
        mainWnd.geometry('1325x950')
        mainWnd.config(bg = 'black')

        #main frame that will encapsulate all the other widgets needed
        self.frame = Frame(mainWnd)
        self.frame.config(width = 1250, height = 940)

        #Create photoimage of the background image
        self.image = ImageTk.PhotoImage(Image.open('Map/cmuBuilding.jpg').resize((1300,940), Image.ANTIALIAS))
        self.label = Label(self.frame, image = self.image)

        
        #Import Images, make them into PhotoImages and Store them
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
        
        #Label that will dislay the map
        #Canvas for the label to be in

        self.canvas = Canvas(self.frame)
        self.canvas.config(width = 1000, height = 750)
        self.canvas.create_image(0,0, image = self.Maps[0], anchor = NW)

        #Create the buttons

        self.currentDisplayedImage = [self.Maps[0]] #This is a reference to a list, which when changed is updated into the variable
        
        self.selectGF = Button(self.frame, command = lambda maps = self.Maps,
                               c = self.canvas: switchFloor(maps, c, self.currentDisplayedImage, 'GF'),
                               text = "Ground Floor", pady = 10)
        
        self.selectF1 = Button(self.frame, command = lambda maps = self.Maps,
                               c = self.canvas: switchFloor(maps, c, self.currentDisplayedImage, 'F1'), 
                               text = "First Floor", pady = 10)


        #List of options, and button to execute request
        self.optionsFrame = Frame(self.frame)
        self.optionList = Listbox(self.optionsFrame)
        self.optionList.config(height = 25, width = 30)

        #Combine all the sections in the first floor and ground floor
        sections = sectionsGF + sectionsF1
        #Sort them - makes it easier for the user to navigate to the section he wants to request
        sections.sort()
        #Add the elements to the listbox
        for section in sections:
            self.optionList.insert(END, section)
        #Button when clicked, gets the active element in the list box and executes the drawShape function
        requestSecBtn = Button(self.optionsFrame, text = 'Request Section',
                               command = lambda : drawShape(self.currentDisplayedImage, self.Maps,
                                                            self.optionList.get(ACTIVE), self.canvas),
                               pady = 5, bg = 'black')

        #update the global variable buttons with all the buttons, excluding the return button
        buttons = [self.selectGF, self.selectF1, requestSecBtn]
        
        #Display Everything
        self.label.grid(row = 0, rowspan = 5, column = 0, columnspan = 5)
        self.canvas.grid(row = 2, column = 1, columnspan = 3)
        self.selectGF.grid(row = 0, column = 1)
        self.selectF1.grid(row = 0, column = 3)
        self.optionsFrame.grid(row = 2, column = 0)
        self.optionList.pack()
        requestSecBtn.pack()

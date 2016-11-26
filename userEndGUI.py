from Tkinter import *
from PIL import Image, ImageTk
import getCarrefourPromotions


#My other functions
import dormLife as DL
import LaundryProgram as LP
import CleaningProgram as CP
import CookingProgram as CKP
import CMUMap as Map
import imp
import CookingProg as CookingProg
import BuyingLife as BL

def printCoor(e):
    print e.x, e.y

#Returns to the main page
def Return():
    global mainWnd
    global openFrames
    global welcomeFrame5
    global buttonsFrame
    global spaceFrame

    spaceFrame.grid(row = 0, column = 0)
    mainWnd.geometry('1500x1500')
    mainWnd.config(bg = 'white')
    for frame in openFrames:
        openFrames[frame].frame.grid_forget()
    buttonsFrame.grid(row = 1, rowspan = 3, column = 1)
    welcomeFrame.grid(row = 0, rowspan = 4, column = 2)
    
    
#Dorm Life------------------------------------------------------------------------------------------------

#Laundy Part of the Program ------------------------------------------------------------------------------

#Displays the Laundry life Frame
def LaundryProgram(openDormLifeFrames):
    global openFrames
    global mainWnd

    #Clear all frames in dorm life to create an open space for this frame
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()

    #IF opening it for the first time
    if 'Laundry' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame() #Frame that the dormLife program is on
        openDormLifeFrames['Laundry'] = LP.LaundryProgram(dormsFrame) #Create the Laundry Life Framej

    #If IF statement is skipped, that means the frame has already been made and established

    #Display frame
    openDormLifeFrames['Laundry'].frame.grid(row = 0, rowspan = 6, column = 3)    
#----------------------------------------------------------------------------------------------------------
#Cleaning Part of the Program -----------------------------------------------------------------------------

#Displays the Cleaning Life Frame
def CleaningProgram(openDormLifeFrames, ):
    global openFrames

    #Clear all frames from the screen (in dormlife)
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()

    #If True, then create the cleaning life frame
    if 'Cleaning' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame()
        openDormLifeFrames['Cleaning'] = CP.CleaningProgram(dormsFrame)
    #Display the frame
    openDormLifeFrames['Cleaning'].frame.grid(row = 0, rowspan = 4, column = 3)


#----------------------------------------------------------------------------------------------------------
#Cooking Part of the Program -----------------------------------------------------------------------------

def cookingProgram(openDormLifeFrames, space):
    global openFrames
    space.grid_forget()
    #Clear all frames from the screen(in dormlife)
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()
    if 'Cooking' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame()
        openDormLifeFrames['Cooking'] = CookingProg.CookingProg(dormsFrame)

    openDormLifeFrames['Cooking'].frame.grid(row = 0, rowspan = 4, column = 3)
    
#----------------------------------------------------------------------------------------------------------

#Executes the dorm life program
def executeDormLifeProg():
    global mainWnd
    global openFrames
    global welcomeFrame
    global buttonsFrame
    #Clear the welcome frame grid (in case it was the first program executed by the user)
    welcomeFrame.grid_forget()
    buttonsFrame.grid_forget()

    #Empty all frames (of the other programs, regardless if it is actually visible or not)
    for frame in openFrames:
        openFrames[frame].frame.grid_forget()
        
    #If not established
    if "DormLife" not in openFrames:

        openDormLifeFrames = {} #Initialize this dictionary that will contain all the frames of the sub-programs in it

        openFrames['DormLife'] = DL.dormLifeProgram(mainWnd) #Create the program
        
        #Adds Functionality to the buttons, because the execution functions are in this file
        openFrames['DormLife'].laundryBtn.config(command = lambda frames = openDormLifeFrames : LaundryProgram(frames))
        openFrames['DormLife'].cleaningBtn.config(command = lambda frames = openDormLifeFrames : CleaningProgram(frames))
        openFrames['DormLife'].cookingBtn.config(command = lambda frames = openDormLifeFrames, spaceFrame = openFrames['DormLife'].spaceFrame: cookingProgram(frames, spaceFrame))

    #Display all the widgets inside the frame (Buttons, labels, etc...)
        openFrames['DormLife'].InstructionalFrame.grid(row = 1, rowspan = 3, column = 0)
        openFrames['DormLife'].spaceFrame.grid(row = 0, column = 2)
        openFrames['DormLife'].title.grid(row = 0, column = 1)
        openFrames['DormLife'].laundryBtn.grid(row = 1, column = 1)
        openFrames['DormLife'].cleaningBtn.grid(row = 2, column = 1)
        openFrames['DormLife'].cookingBtn.grid(row = 3, column = 1)

    #Return Button
        returnButton = Button(openFrames['DormLife'].frame, text = "Return to Main Menu", command = Return)
        returnButton.grid(row = 4, column = 1, pady = 5)

    
        
  #Display the frame
    openFrames['DormLife'].frame.grid(row = 0, rowspan = 4, column = 3)

#----------------------------------------------------------------------------------------------------------
#Open the buying life program
def executeBL():
    global mainWnd
    global openFrames
    global buttonsFrame
    global spaceFrame

    #Hide all the other frames
    welcomeFrame.grid_forget()
    buttonsFrame.grid_forget()
    spaceFrame.grid_forget()
    for someframe in openFrames:
            openFrames[someframe].frame.grid_forget()

    
    #If not open
    if 'BuyingLife' not in openFrames:
        openFrames['BuyingLife'] = BL.BuyingLife(mainWnd) #Open It
        openFrames['BuyingLife'].frame.grid(row = 0, rowspan = 4, column = 1) #Display It
        #Create reurn to menu button
        returnButton = Button(openFrames['BuyingLife'].frame, text = "Return to Main Menu", command = Return)
        returnButton.pack()

    else:
        #adjust geometry of window to thatwanted by the program
        mainWnd.geometry('1325x890')
        mainWnd.config(bg = 'white')
        #Display the frame
        openFrames['BuyingLife'].frame.grid(row = 0, rowspan = 4, column = 1)

    
#----------------------------------------------------------------------------------------------------------

#Cmu Campus Map -------------------------------------------------------------------------------------------

def executeCampusLife():
    global mainWnd
    global openFrames
    global buttonsFrame
    global spaceFrame

    #GHide all other elements
    welcomeFrame.grid_forget()
    buttonsFrame.grid_forget()
    spaceFrame.grid_forget()
    for someframe in openFrames:
            openFrames[someframe].frame.grid_forget()

            
    #If not open
    if 'CampusLife' not in openFrames:
        openFrames['CampusLife'] = Map.CMUMap(mainWnd) #Open
        openFrames['CampusLife'].frame.grid(row = 0, rowspan = 4, column = 1) #Display
        #Create a return to menu button
        returnButton = Button(openFrames['CampusLife'].frame, text = "Return to Main Menu", command = Return)
        returnButton.grid(row = 4, column = 2)
    else:
        #Adjust properties of the window to suit that required by the program
        mainWnd.geometry('1325x950')
        mainWnd.config(bg = 'black')
        #Display it
        openFrames['CampusLife'].frame.grid(row = 0, rowspan = 4, column = 1)

    




#----------------------------------------------------------------------------------------------------------

#Create the program window
mainWnd = Tk()
mainWnd.geometry('1500x1500')
mainWnd.title("Freshman Helper")

# MENU ---------------------------------------------------------------------

#Still under work, but has basic functionality
menubar = Menu(mainWnd)

# Inspired from http://effbot.org/tkinterbook/menu.htm
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit")
menubar.add_cascade(label="Exit", menu=filemenu)

mainWnd.config(menu=menubar)

#---------------------------------------------------------------------------

#The label is like a top padding for the first button
menuLabel = Label(mainWnd, text = "")
menuLabel.config(padx = 5, pady = 5, font = ('Lucida Grande', '50'))


#Frame to House The Frames
buttonsFrame = Frame(mainWnd)
buttonsFrame.config(width = 250)


#Button 1 - This, when clicked will execute the Dorm5 Life Program
dormLife = Button(buttonsFrame, command = executeDormLifeProg)
dormIcon = ImageTk.PhotoImage(Image.open('IconImages/dormButton1.jpg'))
dormLife.config(padx = 5, image = dormIcon)

#Button 2 - This, when clicked, will execute the buying Life Program
buyingLife = Button(buttonsFrame)
buyingIcon = ImageTk.PhotoImage(Image.open('IconImages/CarrefourLuluButton.jpg'))
buyingLife.config(padx = 5, image = buyingIcon, command = executeBL)

#Button 3 - This, when clicked, will execute the Campus Life Program
CMUQMap = Button(buttonsFrame, command = executeCampusLife)
CMUQIcon = ImageTk.PhotoImage(Image.open('IconImages/CMUQButton.jpg'))
CMUQMap.config(padx = 5, image = CMUQIcon)

#Create the welcome frame
welcomeFrame = Frame(mainWnd)
welcomeFrame.config(width = 1250, height = 940, bg = 'white')

#SpacingFrame
spaceFrame = Frame(mainWnd, width = 50)

#Message displayed for the user
message = "Welcome CMUQ Freshman.\n The lonely dorm life you will have will be tough, and outstandingly hard to manage.\n"
message += "This app was created to help you manage your International Life.\n\n"
message += "Dorm Life: Find steps to help you perform your chores:-\n\t1. Laundry\n\t2. Cleaning\n\t3. Cooking\n\n"
message += "Buying Life: Get quick access to the Carrefour and Lulu Shopping Catalogue,\n and a quick access to the latest deals.\n\n"
message += "Campus Life: We provided you with a map of the CMUQ Campus.\nFind quickly the location of classrooms and other campus areas"
welcomeTextLabel = Label(welcomeFrame, text = message)
welcomeTextLabel.config( padx = 150, font = ('Lucida Grande', '25')) #Adjust the size and font


#Display all of the widgets

menuLabel.grid(row = 0, column = 0)
spaceFrame.grid(row = 0, column = 0)
dormLife.pack()
buyingLife.pack()
CMUQMap.pack()
buttonsFrame.grid(row = 1, rowspan = 3, column = 1)
welcomeFrame.grid(row = 0, rowspan = 4, column = 2)
#welcomeFrame.config( padx = 10, relief = GROOVE)
welcomeTextLabel.pack()
welcomeTextLabel.bind('<Button-1>', printCoor)

#Dictionary that will contain reference to all the programs (Dorm life, Campus Life, Cleaning Life)
openFrames = {}

#mainloop for mainWnd
mainWnd.mainloop()

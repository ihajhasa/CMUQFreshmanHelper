from Tkinter import *
import PIL
from PIL import Image, ImageTk


#My other functions
import dormLife as DL
import LaundryProgram as LP
import CleaningProgram as CP
import CookingProgram as CKP
import CMUMap as Map
import imp
import CookingProg as CookingProg


#Def Return:
def Return():
    global openFrames
    global welcomeFrame5
    global buttonsFrame
    for frame in openFrames:
        openFrames[frame].frame.grid_forget()
    buttonsFrame.grid(row = 1, rowspan = 3, column = 1)
    welcomeFrame.grid(row = 0, rowspan = 4, column = 2)
    
    
#Dorm Life---------------------------------------------------------------5---------------------------------

#Laundy Part of the Program ------------------------------------------------------------------------------

#Displays the Laundry life Frame
def LaundryProgram(openDormLifeFrames):
    global openFrames

    #Clear all frames in dorm life to create an open space for this frame
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()

    #IF opening it for the first time
    if 'Laundry' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame() #Frame that the dormLife program is on
        openDormLifeFrames['Laundry'] = LP.LaundryProgram(dormsFrame) #Create the Laundry Life Framej

    #If IF statement is skipped, that means the frame has already been made and established

    #Display frame
    openDormLifeFrames['Laundry'].frame.grid(row = 0, rowspan = 4, column = 2)    
#----------------------------------------------------------------------------------------------------------
#Cleaning Part of the Program -----------------------------------------------------------------------------

#Displays the Cleaning Life Frame
def CleaningProgram(openDormLifeFrames):
    global openFrames

    #Clear all frames from the screen (in dormlife)
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()

    #If True, then create the cleaning life frame
    if 'Cleaning' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame()
        openDormLifeFrames['Cleaning'] = CP.CleaningProgram(dormsFrame)
    #Display the frame
    openDormLifeFrames['Cleaning'].frame.grid(row = 0, rowspan = 4, column = 2)


#----------------------------------------------------------------------------------------------------------
#Cooking Part of the Program -----------------------------------------------------------------------------

def cookingProgram(openDormLifeFrames):
    global openFrames
    #Clear all frames from the screen(in dormlife)
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()
    if 'Cooking' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame()
        openDormLifeFrames['Cooking'] = CookingProg.CookingProg(dormsFrame)

    openDormLifeFrames['Cooking'].frame.grid(row = 0, rowspan = 4, column = 2)
    
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
        openFrames['DormLife'].laundryBtn.config(command = lambda frames = openDormLifeFrames: LaundryProgram(frames))
        openFrames['DormLife'].cleaningBtn.config(command = lambda frames = openDormLifeFrames: CleaningProgram(frames))
        openFrames['DormLife'].cookingBtn.config(command = lambda frames = openDormLifeFrames: cookingProgram(frames))

    #Display all the widgets inside the frame (Buttons, labels, etc...)
        openFrames['DormLife'].title.grid(row = 0, column = 1)
        openFrames['DormLife'].laundryBtn.grid(row = 1, column = 1)
        openFrames['DormLife'].cleaningBtn.grid(row = 2, column = 1)
        openFrames['DormLife'].cookingBtn.grid(row = 3, column = 1)

    #Return Button
        returnButton = Button(openFrames['DormLife'].frame, text = "Return to Main Menu", command = Return)
        returnButton.grid(row = 4, column = 1)

    
        
  #Display the frame
    openFrames['DormLife'].frame.grid(row = 0, rowspan = 4, column = 1)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Cmu Campus Map -------------------------------------------------------------------------------------------

def executeCampusLife():
    global mainWnd
    global openFrames
    global buttonsFrame

    
    welcomeFrame.grid_forget()
    buttonsFrame.grid_forget()

    
    for someframe in openFrames:
            openFrames[someframe].frame.grid_forget()
    
    if 'CampusLife' not in openFrames:
        openFrames['CampusLife'] = Map.CMUMap(mainWnd)
        openFrames['CampusLife'].frame.grid(row = 0, rowspan = 4, column = 1)
    else:
        openFrames['CampusLife'].frame.grid(row = 0, rowspan = 4, column = 1)

    returnButton = Button(openFrames['CampusLife'].frame, text = "Return to Main Menu", command = Return)
    returnButton.grid(row = 4, column = 2)




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

#Button 2 - This, when clicked, will execute the Cleaning Life Program
buyingLife = Button(buttonsFrame)
buyingIcon = ImageTk.PhotoImage(Image.open('IconImages/CarrefourLuluButton.jpg'))
buyingLife.config(padx = 5, image = buyingIcon)

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

#Dictionary that will contain reference to all the programs (Dorm life, Campus Life, Cleaning Life)
openFrames = {}

#mainloop for mainWnd
mainWnd.mainloop()

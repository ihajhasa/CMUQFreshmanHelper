from Tkinter import *
from PIL import Image, ImageTk
import dormLife as DL
import LaundryProgram as LP
import CleaningProgram as CP
import CookingProgram as CKP
import CMUMap as Map

#Dorm Life------------------------------------------------------------------------------------------------

#Laundy Part of the Program ------------------------------------------------------------------------------

def LaundryProgram(openDormLifeFrames):
    global openFrames
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()

    if 'Laundry' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame()
        openDormLifeFrames['Laundry'] = LP.LaundryProgram(dormsFrame)

    openDormLifeFrames['Laundry'].frame.grid(row = 0, rowspan = 4, column = 2)
    
#----------------------------------------------------------------------------------------------------------
#Cleaning Part of the Program -----------------------------------------------------------------------------

def CleaningProgram(openDormLifeFrames):
    global openFrames
    
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()

    if 'Cleaning' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame()
        openDormLifeFrames['Cleaning'] = CP.CleaningProgram(dormsFrame)

    openDormLifeFrames['Cleaning'].frame.grid(row = 0, rowspan = 4, column = 2)


#----------------------------------------------------------------------------------------------------------
#Cooking Part of the Program -----------------------------------------------------------------------------
        
def CookingProgram(openDormLifeFrames):
    global openFrames
    
    for i in openDormLifeFrames:
        openDormLifeFrames[i].frame.grid_forget()

    if 'Cooking' not in openDormLifeFrames:
        dormsFrame = openFrames['DormLife'].getFrame()
        openDormLifeFrames['Cooking'] = CKP.cookingProgram(dormsFrame)

    openDormLifeFrames['Cooking'].frame.grid(row = 0, rowspan = 4, column = 2)


#----------------------------------------------------------------------------------------------------------
def executeDormLifeProg():
    global mainWnd
    global openFrames
    global welcomeFrame

    welcomeFrame.grid_forget()
    
    for frame in openFrames:
        openFrames[frame].frame.grid_forget()
        
    
    if "DormLife" not in openFrames:

        openDormLifeFrames = {}

        openFrames['DormLife'] = DL.dormLifeProgram(mainWnd)
        
        #Adds Functionality to the button
        openFrames['DormLife'].laundryBtn.config(command = lambda frames = openDormLifeFrames: LaundryProgram(frames))
        openFrames['DormLife'].cleaningBtn.config(command = lambda frames = openDormLifeFrames: CleaningProgram(frames))
        openFrames['DormLife'].cookingBtn.config(command = lambda frames = openDormLifeFrames: CookingProgram(frames))


        #openFrames['DormLife'].frame.grid(row = 0, rowspan = 4, column = 2)
        openFrames['DormLife'].title.grid(row = 0, column = 1)
        openFrames['DormLife'].laundryBtn.grid(row = 1, column = 1)
        openFrames['DormLife'].cleaningBtn.grid(row = 2, column = 1)
        openFrames['DormLife'].cookingBtn.grid(row = 3, column = 1)

    
        
  
    openFrames['DormLife'].frame.grid(row = 0, rowspan = 4, column = 1)

#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Cmu Campus Map -------------------------------------------------------------------------------------------

def executeCampusLife():
    global mainWnd
    global openFrames

    welcomeFrame.grid_forget()
    for someframe in openFrames:
            openFrames[someframe].frame.grid_forget()
    
    if 'CampusLife' not in openFrames:
        openFrames['CampusLife'] = Map.CMUMap(mainWnd)
        openFrames['CampusLife'].frame.grid(row = 0, rowspan = 4, column = 7)
    else:
        openFrames['CampusLife'].frame.grid(row = 0, rowspan = 4, column = 7)
        





#----------------------------------------------------------------------------------------------------------

mainWnd = Tk()
#mainWnd.attributes("-fullscreen", True)
mainWnd.geometry('1500x1500')
mainWnd.title("Freshman Helper")

helpSheet = ''

# MENU ---------------------------------------------------------------------
menubar = Menu(mainWnd)

# Inspired from http://effbot.org/tkinterbook/menu.htm
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit")
menubar.add_cascade(label="Exit", menu=filemenu)

mainWnd.config(menu=menubar)

#---------------------------------------------------------------------------

menuLabel = Label(mainWnd, text = "")
menuLabel.config(padx = 5, pady = 5, font = ('Lucida Grande', '50'))

dormLife = Button(mainWnd, command = executeDormLifeProg)
dormIcon = ImageTk.PhotoImage(Image.open('IconImages/dormButton1.jpg'))
dormLife.config(padx = 5, image = dormIcon)

buyingLife = Button(mainWnd)
buyingIcon = ImageTk.PhotoImage(Image.open('IconImages/CarrefourLuluButton.jpg'))
buyingLife.config(padx = 5, image = buyingIcon)

CMUQMap = Button(mainWnd, command = executeCampusLife)
CMUQIcon = ImageTk.PhotoImage(Image.open('IconImages/CMUQButton.jpg'))
CMUQMap.config(padx = 5, image = CMUQIcon)

welcomeFrame = Frame(mainWnd)
welcomeFrame.config(width = 1250, height = 940, bg = 'white')
message = "Welcome CMUQ Freshman.\n The lonely dorm life you will have will be tough, and outstandingly hard to manage.\n"
message += "This app was created to help you manage your International Life.\n\n"
message += "Dorm Life: Find steps to help you perform your chores:-\n\t1. Laundry\n\t2. Cleaning\n\t3. Cooking\n\n"
message += "Buying Life: Get quick access to the Carrefour and Lulu Shopping Catalogue,\n and a quick access to the latest deals.\n\n"
message += "Campus Life: We provided you with a map of the CMUQ Campus.\nFind quickly the location of classrooms and other campus areas"
welcomeTextLabel = Label(welcomeFrame, text = message)
welcomeTextLabel.config( padx = 150, font = ('Lucida Grande', '25'))


menuLabel.grid(row = 0, column = 0)
dormLife.grid(row = 1, column = 0)
buyingLife.grid(row = 2, column = 0)
CMUQMap.grid(row = 3, column = 0)
welcomeFrame.grid(row = 0, rowspan = 4, column = 1)
welcomeTextLabel.pack()


openFrames = {}


mainWnd.mainloop()

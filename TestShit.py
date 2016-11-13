from Tkinter import *
from PIL import Image, ImageTk

imageReferences = {}
symbolWnd = Tk()
symbolWnd.geometry('1920x1080')
imageReferences['symbols'] = ImageTk.PhotoImage(Image.open('LaundrySymbolSheetImages/HelpSheetSymbol.jpg'))
labelForImage = Label(symbolWnd, image = imageReferences['symbols'])
labelForImage.pack()
symbolWnd.mainloop()

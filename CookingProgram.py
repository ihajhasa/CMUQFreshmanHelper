import webbrowser
from Tkinter import *
from PIL import Image, ImageTk

class cookingProgram:


    def __init__(self, dormFrame):


        def goToZomato(e):
            if (e.x >= 447 and e.y >= 117) and (e.x <= 680 and e.y <= 330):
                url = 'https://www.zomato.com/doha'
                webbrowser.open_new_tab(url)
            elif e.x >=14 and e.x <= 94: #Since they are all in the same row
                if e.y >=115 and e.y <= 194:
                    url = 'https://www.zomato.com/doha/mcdonalds-1-al-rayyan'
                    webbrowser.open_new_tab(url)
                elif e.y >= 216 and e.y <= 296:
                    url = 'https://www.zomato.com/doha/house-of-tea-al-rayyan/menu'
                    webbrowser.open_new_tab(url)
                elif e.y >= 311 and e.y <= 401:
                    url = 'https://www.zomato.com/doha/restaurants/burger-king?ref_type=subzone&ref_id=62023'
                    webbrowser.open_new_tab(url)

        self.frame = Frame(dormFrame)


        self.displayImage = ImageTk.PhotoImage(Image.open('Cooking/cooking.jpg'))
        self. displayLabel = Label(self.frame, image = self.displayImage)
        self.displayLabel.bind('<Button-1>', goToZomato)

        self.displayLabel.pack()
        

from Tkinter import *
import random
import ZomatoAPIHandler as Z
import Restaurant as R
def prepareNearbyRestaurants(canvas):
    nearbyRestaurants = Z.nearbyRestaurants()
    choices = []
    if 3 <= len(nearbyRestaurants):
        for i in range(1,4):
            choice = random.randint(1,len(nearbyRestaurants) - 1)
            #while choice not in choices:
#               choice = random.randint(1,len(nearbyRestaurants) - 1) 
            choices += [choice]
    #This will house the randomly chosen restaurants            
    restaurants = []
    #The randomly chosen restauants are processed and stored in the restaurants list
    for choice in choices:
        r = Z.createRestaurant(nearbyRestaurants[choice])
        r.makeThumbnail(canvas)
        restaurants += [r]
    return restaurants
            
        
    

class CookingProg:
    #The main frame of the program
    def __init__(self, window):
        self.frame = Frame(window)

        self.canvas = Canvas(self.frame)
        self.canvas.config(width = self.frame.winfo_width())

        self.nearbyRestLabel = Label(self.canvas, text ='Nearby Restaurants')
        self.nearbyRestLabel.config(font = ('Lucida Grande', '25'))
        self.nearbyRestLabel.grid(row = 0, column = 0, columnspan = 3)
        
        self.nearbyRest = prepareNearbyRestaurants(self.canvas)
        i = 0
        for restaurant in self.nearbyRest:
            restaurant.frame.grid(row = 1, column = i)
            i = i + 1
        self.canvas.pack()       

from Tkinter import *
import random
import ZomatoAPIHandler as ZomatoAPI
import Restaurant as R
import tkMessageBox as MB

def hideElements(restaurant):
    restaurant.frame.grid_forget()

def getRequestCategory(categoryReq, options, canvas, request):
    for i in request:
        i.frame.grid_forget()
    idReq = getID(categoryReq, options)
    url = 'https://developers.zomato.com/api/v2.1/search?lat=25.3106&lon=51.446&radius=5000&category='
    url = url + str(idReq)
    results = ZomatoAPI.search(url)
    displayInit =  prepareRestaurants(Restaurants = results, canvas = canvas)
    i = 1
    print displayInit
    if displayInit != []:
        for choice in displayInit:
            choice.frame.grid(row = 4, column = i)
            request += [choice]
            i += 1
    else:
        MB.showerror(title = 'No Results', message = 'There are no restaurants that fit this category.')

def getID(categoryReq, options):
    for category in options:
        if category['name'] == categoryReq:
            return category['id']


def prepareRestaurants(Restaurants = ZomatoAPI.nearbyRestaurants(), canvas = '', num = 3):
    choices = []
    if num <= len(Restaurants):
        for i in range(num):
            choiceKey = random.choice(Restaurants.keys())
            choiceData = Restaurants[choiceKey]
            del Restaurants[choiceKey]
            choices += [choiceData]
    else:
        for i in Restaurants:
            choices += [Restaurants[i]]
            del Restaurants[i]

            
    #This will house the randomly chosen restaurants            
    restaurants = []

    
    #The randomly chosen restauants are processed and stored in the restaurants list
    for choice in choices:
        r = ZomatoAPI.createRestaurant(choice)
        r.makeThumbnail(canvas)
        restaurants += [r]
    return restaurants

def getCategories():
    return ZomatoAPI.getCategories()

class CookingProg:
    #The main frame of the program
    def __init__(self, window):
        self.frame = Frame(window)
        self.frame.config(padx = 40)
        

        self.canvas = Canvas(self.frame)
        self.canvas.config(width = self.frame.winfo_width())

        joke = Label(self.canvas, text ='HAHAHAHAHAHAHA Nice Joke ... Nobody in Karam Hall Cooks Food\nHere are some restaurant recommendations anda mini restaurant search engine')
        joke.config(font = ('Lucida Grande', '21'))
        self.nearbyRestLabel = Label(self.canvas, text ='Nearby Restaurants')
        self.nearbyRestLabel.config(font = ('Lucida Grande', '25'))
        
        
        self.nearbyRest = prepareRestaurants(canvas = self.canvas, num = 4)
        self.request = []
        
        i = 0
        for restaurant in self.nearbyRest:
            restaurant.frame.grid(row = 2, column = i)
            i = i + 1
        
        joke.grid(row = 0, column = 0, columnspan = 4)
        self.nearbyRestLabel.grid(row = 1, column = 0, columnspan = 4)

        #Mini Search engine
        self.searchLabel = Label(self.canvas, text = "Search Restaurant by Category")
        self.searchLabel.config(font = ('Lucida Grande', '25'), pady = 5)

        
        self.listBoxCanvas = Canvas(self.canvas, bd = 5, relief = GROOVE)

        self.miniSearch = getCategories()
        scrollbar = Scrollbar(self.listBoxCanvas)
        scrollbar.pack(fill = Y, side = RIGHT)
        self.categoryListBox = Listbox(self.listBoxCanvas, relief = GROOVE,
                                       selectmode=SINGLE, width = 28,
                                       yscrollcommand = scrollbar.set)
        scrollbar.config(command= self.categoryListBox.yview)
        for category in self.miniSearch:
            self.categoryListBox.insert(END, category['name'])

        

        sendRequestBtn = Button(self.canvas, text = 'Request Restaurant',
                                command = lambda : getRequestCategory(self.categoryListBox.get(ACTIVE),
                                                                      self.miniSearch,
                                                                      self.canvas,
                                                                      self.request))        

        clearRequestBtn = Button(self.canvas, text = "Clear results",
                                      command = lambda : map(hideElements, self.request))

        
        self.categoryListBox.pack()
        self.searchLabel.grid(row = 3, column = 0, columnspan = 4)
        self.listBoxCanvas.grid(row = 4, column = 0)
        sendRequestBtn.grid(row = 5, column = 0)
        clearRequestBtn.grid(row = 5, column = 2)
        
        
        self.canvas.pack()



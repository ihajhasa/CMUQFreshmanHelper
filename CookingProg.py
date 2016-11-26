from Tkinter import *
import random
import ZomatoAPIHandler as ZomatoAPI
import Restaurant as R
import tkMessageBox as MB

#This hides the restaurant (by removing it from the grid)
def hideElements(restaurant):
    restaurant.frame.grid_forget()

#Retrieve restaurants that fit in the user's requested category and choose any 4 at random
def getRequestCategory(categoryReq, options, canvas, request):
    
    #Forget all of the currently displayed options
    for i in request:
        i.frame.grid_forget()
    
    idReq = getID(categoryReq, options) #Get the id of the category
    url = 'https://developers.zomato.com/api/v2.1/search?lat=25.3106&lon=51.446&radius=10000&category='
    url = url + str(idReq)#add the id to the URL
    results = ZomatoAPI.search(url) #get the results from Zomato by sending the url using the search function in ZomatosAPIHandler
    displayInit =  prepareRestaurants(Restaurants = results, canvas = canvas) #Execute the prepare restaurants for display
    i = 1
    #Display the restaurants if there are any
    if displayInit != []:
        for choice in displayInit:
            choice.frame.grid(row = 4, column = i)
            request += [choice]
            i += 1
    else:
        MB.showerror(title = 'No Results', message = 'There are no restaurants that fit this category.')

#Gets the ID of zomato's elements
def getID(categoryReq, options):
    #Options is a dict with kay name of category and id as value
    for category in options:
        if category['name'] == categoryReq:
            return category['id']


def prepareRestaurants(Restaurants = ZomatoAPI.nearbyRestaurants(), canvas = '', num = 3):
    choices = []
    #Choose num amount of restaurants ffrom restaurants
    if num <= len(Restaurants):
        for i in range(num):
            choiceKey = random.choice(Restaurants.keys()) #Randomly choose key for restaurant
            choiceData = Restaurants[choiceKey] #choose that restaurant
            del Restaurants[choiceKey] #delete it from the main dict, so it wont be chosen again
            choices += [choiceData] #add it to the choices list
    else:
        for i in Restaurants:
            choices += [Restaurants[i]]
            del Restaurants[i]

            
    #This will house the randomly chosen restaurants, after the choice is made into a restaurant object           
    restaurants = []

    
    #The randomly chosen restauants are processed and stored in the restaurants list
    for choice in choices:
        r = ZomatoAPI.createRestaurant(choice) #Make the restaurant
        r.makeThumbnail(canvas) #make its thumbnail
        restaurants += [r] #add it to restaurants
    
    return restaurants

#Get the cetgories list from Zomato
def getCategories():
    return ZomatoAPI.getCategories()

class CookingProg:
    #The main frame of the program
    def __init__(self, window):

        #main Frame that will house all the elemnts of this program
        self.frame = Frame(window)
        self.frame.config(padx = 40)
        
        #main canvas that will have all of the elements in it
        self.canvas = Canvas(self.frame)
        self.canvas.config(width = self.frame.winfo_width())

        
        #Cretae the label that has the joke and briefly explains this program
        joke = Label(self.canvas, text ='HAHAHAHAHAHAHA Nice Joke ... Nobody in Karam Hall Cooks Food\nHere are some restaurant recommendations and a mini restaurant search tool')
        joke.config(font = ('Lucida Grande', '21'))

        #Nearby Restaurants Label
        self.nearbyRestLabel = Label(self.canvas, text ='Nearby Restaurants')
        self.nearbyRestLabel.config(font = ('Lucida Grande', '25'))
        
        #Get nearby restaurants
        self.nearbyRest = prepareRestaurants(canvas = self.canvas, num = 4)
        self.request = []
        #Display them
        i = 0
        for restaurant in self.nearbyRest:
            restaurant.frame.grid(row = 2, column = i)
            i = i + 1
        #Grid the joke and restaurants
        joke.grid(row = 0, column = 0, columnspan = 4)
        self.nearbyRestLabel.grid(row = 1, column = 0, columnspan = 4)

        #Mini Search engine
        self.searchLabel = Label(self.canvas, text = "Search Restaurant by Category")
        self.searchLabel.config(font = ('Lucida Grande', '25'), pady = 5)

        #Canvas that will house the list box and scrollbar
        self.listBoxCanvas = Canvas(self.canvas, bd = 5, relief = GROOVE)
        self.miniSearch = getCategories()
        #Set-up scrollbar for the listbox
        scrollbar = Scrollbar(self.listBoxCanvas)
        scrollbar.pack(fill = Y, side = RIGHT)
        #List box will contain all available categories
        self.categoryListBox = Listbox(self.listBoxCanvas, relief = GROOVE,
                                       selectmode=SINGLE, width = 28,
                                       yscrollcommand = scrollbar.set)
        scrollbar.config(command= self.categoryListBox.yview)
        #Add all cateories to the list box
        for category in self.miniSearch:
            self.categoryListBox.insert(END, category['name'])

        

        sendRequestBtn = Button(self.canvas, text = 'Request Restaurant',
                                command = lambda : getRequestCategory(self.categoryListBox.get(ACTIVE),
                                                                      self.miniSearch,
                                                                      self.canvas,
                                                                      self.request))        

        clearRequestBtn = Button(self.canvas, text = "Clear results",
                                      command = lambda : map(hideElements, self.request))

        #Display all the remaining elements
        self.categoryListBox.pack()
        self.searchLabel.grid(row = 3, column = 0, columnspan = 4)
        self.listBoxCanvas.grid(row = 4, column = 0)
        sendRequestBtn.grid(row = 5, column = 0)
        clearRequestBtn.grid(row = 5, column = 2)
        
        #Pack canvas into frame
        self.canvas.pack()



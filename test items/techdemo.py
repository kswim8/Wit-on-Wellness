import module_manager
module_manager.review()
import requests, json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
from matplotlib import pyplot as plt
import bs4
import cmu_112_graphics
import scipy

from cmu_112_graphics import *

class MyApp(App):
    def appStarted(self):
        url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOoIC-4bny-KdZnre_pDz4nTePwVe7YIDfb1INaIJQSFCfAjCxPY-i2Av68w&amp;s'
        # self.image1 = self.loadImage(url)
        # self.image2 = self.scaleImage(self.image1, 2/3)
        self.message = 'Click mouse to enter food'
        self.foodentered = False
        self.foodFullDict = dict() 
        self.index = 0

    def resizeAndDrawPics(self, canvas, cx, cy):
        if self.foodentered:
            for foodname in self.foodFullDict:
                self.index += 1
                canvas.create_image(cx, cy + self.index*50, image=ImageTk.PhotoImage(self.loadImage(self.foodFullDict[foodname][1])))
        
    def redrawAll(self, canvas):
        font = 'Arial 24 bold'
        # canvas.create_image(200, 300, image=ImageTk.PhotoImage(self.image1))
        # canvas.create_image(500, 300, image=ImageTk.PhotoImage(self.image2))
        canvas.create_text(self.width/2,  self.height/2,
                           text=self.message, font=font)
        self.resizeAndDrawPics(canvas, 250, 0)
    
    def getFoodDict(self, userinput):
        

    def mousePressed(self, event):
        userinput = self.getUserInput("What did you eat or drink today? ")

        # CITATION: https://github.com/USDA/USDA-APIs/issues/64
        # pulling food data from the API
        params = {'api_key': 'xva7eCmcY6On4IRr0o28hpJJLJpQXC1nYebWx4Wa'}
        data = {'generalSearchInput': userinput}
        response = requests.post(
            r'https://api.nal.usda.gov/fdc/v1/foods/search',
            params = params,
            json = data
        )

        if (userinput == None) or len(userinput) == 0:
            pass
        else:
            self.foodentered = True
            # create a set to prevent duplicates from showing up
            num = 0
            foodset = set()
            # return top 10 results max using try except so list can be len(10-)
            try:
                while len(foodset) < 10:
                    # get the name of the foods 
                    foodname = response.json()['foods'][num]['description']
                    foodset.add(foodname)
                    num += 1

                    # prints nutrients
                    nutrients = response.json()['foods'][num]['foodNutrients']
                    # iterate through nutrient dicts in the nutrients list
                    for nutrientDict in nutrients:
                        # if nutrient Id matches desired num, store to protein/fat/content var
                        if nutrientDict['nutrientId'] == 1003:
                            proteinContent = nutrientDict['value']
                        elif nutrientDict['nutrientId'] == 1004:
                            fatContent = nutrientDict['value']
                        elif nutrientDict['nutrientId'] == 1005:
                            carbContent = nutrientDict['value']
                    # add a key value pair for the food with tuple of protein/fat/content
                    self.foodFullDict[foodname] = (proteinContent, fatContent, carbContent)

            except IndexError:
                # if there are no search results, print this and repeat
                if len(foodset) == 0:
                    self.showMessage(f"Could not find a food or drink labeled {userinput}, please try again.")
                # otherwise, there's probably some single or <10 elements
            
            # print(foodset) # final list of foods to display
            # print(foodFullDict) # final list of foods with protein/fat/carb

            # CITATION: https://stackoverflow.com/questions/21530274/format-for-a-url-that-goes-to-google-image-search
            # web scrape for the image
            for foodname in foodset:
                imagerequest = requests.get(f'https://www.google.com/search?tbm=isch&q={foodname}%20food%20or%20drink')
                soup = bs4.BeautifulSoup(imagerequest.text, 'html.parser')
                firstimage = soup.find_all("img")[1]
                firstimage = str(firstimage)
                srcindex = firstimage.find('http')
                foodimageurl = firstimage[srcindex:-3] # parsing for url of image   
                self.foodFullDict[foodname] = [self.foodFullDict[foodname], firstimage[srcindex:-3]]

            print(self.foodFullDict) # final food dict with macros + image url

    def testFoodAPI():
        while True:
            # take a user input
            userinput = input("What did you eat or drink today? ")

            # CITATION: https://github.com/USDA/USDA-APIs/issues/64
            # pulling food data from the API
            params = {'api_key': 'xva7eCmcY6On4IRr0o28hpJJLJpQXC1nYebWx4Wa'}
            data = {'generalSearchInput': userinput}
            response = requests.post(
                r'https://api.nal.usda.gov/fdc/v1/foods/search',
                params = params,
                json = data
            )
            # now we have a dict of the search results

            # create a set to prevent duplicates from showing up
            num = 0
            foodset = set()
            foodFullDict = dict()
            # return top 10 results max using try except so list can be len(10-)
            try:
                while len(foodset) < 10:
                    # get the name of the foods 
                    foodname = response.json()['foods'][num]['description']
                    foodset.add(foodname)
                    num += 1

                    # prints nutrients
                    nutrients = response.json()['foods'][num]['foodNutrients']
                    # iterate through nutrient dicts in the nutrients list
                    for nutrientDict in nutrients:
                        # if nutrient Id matches desired num, store to protein/fat/content var
                        if nutrientDict['nutrientId'] == 1003:
                            proteinContent = nutrientDict['value']
                        elif nutrientDict['nutrientId'] == 1004:
                            fatContent = nutrientDict['value']
                        elif nutrientDict['nutrientId'] == 1005:
                            carbContent = nutrientDict['value']
                    # add a key value pair for the food with tuple of protein/fat/content
                    foodFullDict[foodname] = (proteinContent, fatContent, carbContent)

            except IndexError:
                # if there are no search results, print this and repeat
                if len(foodset) == 0:
                    print(f"Could not find a food or drink labeled {userinput}, please try again.")
                # otherwise, there's probably some single or <10 elements
            
            print(foodset) # final list of foods to display
            print(foodFullDict) # final list of foods with protein/fat/carb

            # CITATION: https://stackoverflow.com/questions/21530274/format-for-a-url-that-goes-to-google-image-search
            # web scrape for the image
            for foodname in foodset:
                imagerequest = requests.get(f'https://www.google.com/search?tbm=isch&q={foodname}%20food%20or%20drink')
                soup = bs4.BeautifulSoup(imagerequest.text, 'html.parser')
                firstimage = soup.find_all("img")[1]
                firstimage = str(firstimage)
                srcindex = firstimage.find('http')
                foodimageurl = firstimage[srcindex:-3] # parsing for url of image   
                foodFullDict[foodname] = [foodFullDict[foodname], firstimage[srcindex:-3]]

            print(foodFullDict)

            # plan on displaying the images with the food items in a nice UI
    
    def getHashables(self):
        return (self.x, ) # return a tuple of hashables
    def __hash__(self):
        return hash(self.getHashables())
    def __eq__(self, other):
        return (isinstance(other, A) and (self.x == other.x))

MyApp(width=700, height=600)

# testing out FDC API and getting data 
def testFoodAPI():
    while True:
        # take a user input
        userinput = input("What did you eat or drink today? ")

        # CITATION: https://github.com/USDA/USDA-APIs/issues/64
        # pulling food data from the API
        params = {'api_key': 'xva7eCmcY6On4IRr0o28hpJJLJpQXC1nYebWx4Wa'}
        data = {'generalSearchInput': userinput}
        response = requests.post(
            r'https://api.nal.usda.gov/fdc/v1/foods/search',
            params = params,
            json = data
        )
        # now we have a dict of the search results

        # create a set to prevent duplicates from showing up
        num = 0
        foodset = set()
        foodFullDict = dict()
        # return top 10 results max using try except so list can be len(10-)
        try:
            while len(foodset) < 10:
                # get the name of the foods 
                foodname = response.json()['foods'][num]['description']
                foodset.add(foodname)
                num += 1

                # prints nutrients
                nutrients = response.json()['foods'][num]['foodNutrients']
                # iterate through nutrient dicts in the nutrients list
                for nutrientDict in nutrients:
                    # if nutrient Id matches desired num, store to protein/fat/content var
                    if nutrientDict['nutrientId'] == 1003:
                        proteinContent = nutrientDict['value']
                    elif nutrientDict['nutrientId'] == 1004:
                        fatContent = nutrientDict['value']
                    elif nutrientDict['nutrientId'] == 1005:
                        carbContent = nutrientDict['value']
                # add a key value pair for the food with tuple of protein/fat/content
                foodFullDict[foodname] = (proteinContent, fatContent, carbContent)

        except IndexError:
            # if there are no search results, print this and repeat
            if len(foodset) == 0:
                print(f"Could not find a food or drink labeled {userinput}, please try again.")
            # otherwise, there's probably some single or <10 elements
        
        print(foodset) # final list of foods to display
        print(foodFullDict) # final list of foods with protein/fat/carb

        # CITATION: https://stackoverflow.com/questions/21530274/format-for-a-url-that-goes-to-google-image-search
        # web scrape for the image
        for foodname in foodset:
            imagerequest = requests.get(f'https://www.google.com/search?tbm=isch&q={foodname}%20food%20or%20drink')
            soup = bs4.BeautifulSoup(imagerequest.text, 'html.parser')
            firstimage = soup.find_all("img")[1]
            firstimage = str(firstimage)
            srcindex = firstimage.find('http')
            foodimageurl = firstimage[srcindex:-3] # parsing for url of image   
            foodFullDict[foodname] = [foodFullDict[foodname], firstimage[srcindex:-3]]

        print(foodFullDict)

        # plan on displaying the images with the food items in a nice UI

def testNumpy():
    pass

def testPIL():

    pass

def matplottest():

    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2,1]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()

def matplottest2():
     
    x = ['Carbohydrates','Proteins','Fats'] 
    y = [12,16,6]  

    # x2 = [6,9,11] 
    # y2 = [6,15,7] 
    plt.bar(x, y, align = 'center') 
    # plt.bar(x2, y2, color = 'g', align = 'center') 
    plt.title('Bar graph') 
    plt.ylabel('Y axis') 
    plt.xlabel('X axis')  

    plt.show()

# CITATION: https://codeloop.org/how-to-create-textbox-in-python-tkinter/
# testing out an integrated text box and responsive button
def textBoxTest():
    window = tk.Tk()

    window.title("Top Level App")
    window.minsize(600,400)

    def clickMe():
        label.configure(text= 'Hello ' + name.get())

    label = ttk.Label(window, text = "Enter name: ")
    label.grid(column = 0, row = 0)

    name = tk.StringVar()
    nameEntered = ttk.Entry(window, width = 50, textvariable = name)
    nameEntered.grid(column = 0, row = 1)


    button = ttk.Button(window, text = "Click Me", command = clickMe)
    button.grid(column= 0, row = 2)

    window.mainloop()


# textBoxTest()
# testFoodAPI()
testNumpy()
testPIL()
# matplottest()
# matplottest2()



# class Food(object):

#     def __init__(self):
#         self.userinput = input("What did you eat or drink today? ")
    
#     # CITATION: https://github.com/USDA/USDA-APIs/issues/64
#     params = {'api_key': 'xva7eCmcY6On4IRr0o28hpJJLJpQXC1nYebWx4Wa'}
#     data = {'generalSearchInput': userinput}
#     response = requests.post(
#         r'https://api.nal.usda.gov/fdc/v1/foods/search',
#         params = params,
#         json = data
#     )

#     def getFoodName(self):
#         return response.json()['foods'][num]['description']
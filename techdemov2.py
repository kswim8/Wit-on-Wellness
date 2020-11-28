# Keren Huang - Tech Demo, TP0

# Alex's suggestions moving forward:
#       currently, scipy does too much of the heavy lifting
#       find some way to go beyond just using this to add complexity
#       tip: implement my own linear programming system
#       create ML model --> how good is the diet? find datasets off kaggle
#       make a recommendation for the user; on top of "you need more ___"
#       give examples of foods the user could try for more macros for their goal

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

############################################################################
# USING NUMPY, PANDAS, AND MATPLOTLIB

# check tp_v2.py for demo

class MyApp(App):
    def appStarted(self):
        self.message = 'Click here to enter a food or drink!'
        self.foodentered = False
        self.foodFullDict = dict() 

    ############################################################################
    # USING PIL:

    # CITATION: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#cachingPhotoImages
    def getCachedPhotoImage(self, image):
        # stores a cached version of the PhotoImage in the PIL/Pillow image
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def resizeAndDrawPics(self, canvas):
        if self.foodentered:
            for foodname in self.foodFullDict:
                # cache the image
                resizedImage = self.scaleImage(self.loadImage(self.foodFullDict[foodname][1]), 0.5)
                cachedResizedImage = self.getCachedPhotoImage(resizedImage)
                # create the cached image
                canvas.create_image(250, self.foodFullDict[foodname][2], image=cachedResizedImage)

    def redrawAll(self, canvas):
        font = 'Arial 14 bold'
        canvas.create_rectangle(self.width/2, 5, self.width, 50)
        canvas.create_text(3*self.width/4,  25,
                            text=self.message, font=font)
        self.resizeAndDrawPics(canvas)

    ############################################################################
    # USING REQUESTS AND JSON AND BEAUTIFUL SOUP:

    def getFoodDict(self, userinput):
        # CITATION: https://github.com/USDA/USDA-APIs/issues/64
        # pulling food data from the API
        params = {'api_key': 'xva7eCmcY6On4IRr0o28hpJJLJpQXC1nYebWx4Wa'}
        data = {'generalSearchInput': userinput}
        response = requests.post(
            r'https://api.nal.usda.gov/fdc/v1/foods/search',
            params = params,
            json = data
        )        

        self.foodentered = True
        self.foodFullDict = dict()
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
                print(nutrients)
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

        # CITATION: https://stackoverflow.com/questions/21530274/format-for-a-url-that-goes-to-google-image-search
        # web scrape for the image
        picCy = 50 # embed the locations of where they will be placed using picCy
        for foodname in foodset:
            imagerequest = requests.get(f'https://www.google.com/search?tbm=isch&q={foodname}%20food%20or%20drink')
            soup = bs4.BeautifulSoup(imagerequest.text, 'html.parser')
            firstimage = soup.find_all("img")[1]
            firstimage = str(firstimage)
            srcindex = firstimage.find('http')      # parsing for start of link
            foodimageurl = firstimage[srcindex:-3]  # slicing for url of image   
            self.foodFullDict[foodname] = [self.foodFullDict[foodname], firstimage[srcindex:-3], picCy] # assign value to key
            picCy += 75    

        print(self.foodFullDict) # final food dict with macros + image url

    def mousePressed(self, event):
        if (self.width/2 <= event.x <= self.width) and (0 <= event.y <= 50):
            userinput = self.getUserInput("What did you eat or drink today? ")
    
            if (userinput == None) or len(userinput) == 0:
                pass
            else:
                self.getFoodDict(userinput) 
            
    def getHashables(self):
        return (self.x, ) # return a tuple of hashables

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        return (isinstance(other, A) and (self.x == other.x))

MyApp(width=700, height=600)

############################################################################
# USING SCIPY AND OPTIMIZE:

# CITATION: https://towardsdatascience.com/solving-your-first-linear-program-in-python-9e3020a9ad32
from scipy.optimize import linprog
import numpy as np

# creating a strawberry banana smoothie

# Equations to solve
# variables: s = strawberries, b = bananas, m = milk, y = yogurt
# s + b + m + y = 75 (all ingredients summed should be 75 g)
# y - 2m = 0 (yogurt is 2x milk)
# s + b <= 50 (strawberry + banana is no more than 50 g)
# s + y <= 30 (strawberry + yogurt is no more than 30 g)
# s - b + m - y <= 0 (sum of strawberry and milk is no more than sum of banana and yogurt)

# X matrix
var_list = ['Strawberries', 'Bananas', 'Milk', 'Yogurt']

# Inequality equations, LHS
A_ineq = [[1., 1., 0., 0.], [1., 0., 0., 1.], [1., -1., 1., -1.]]

# Inequality equations, RHS
B_ineq = [50., 30., 0.]

# Equality equations, LHS
A_eq = [[1., 1., 1., 1.], [0., 0., -2., 1.]]

# Equality equations, RHS
B_eq = [75., 0.]

# Cost function
c = [0., 0., 1., 1.]  # construct a cost function

print('WITHOUT BOUNDS')
# pass these matrices to linprog, use the method 'interior-point'. '_ub' implies 
# the upper-bound or inequality matrices and '_eq' imply the equality matrices
res_no_bounds = linprog(c, A_ub=A_ineq, b_ub=B_ineq, A_eq=A_eq, b_eq=B_eq, method='interior-point')
print(res_no_bounds)
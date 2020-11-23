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
    
    def getCachedPhotoImage(self, image):
        # stores a cached version of the PhotoImage in the PIL/Pillow image
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def resizeAndDrawPics(self, canvas):
        if self.foodentered:
            for foodname in self.foodFullDict:
                canvas.create_image(250, self.foodFullDict[foodname][2], image=ImageTk.PhotoImage(self.loadImage(self.foodFullDict[foodname][1])))
        
    def redrawAll(self, canvas):
        font = 'Arial 24 bold'
        cy = 0
        # canvas.create_image(200, 300, image=ImageTk.PhotoImage(self.image1))
        # canvas.create_image(500, 300, image=ImageTk.PhotoImage(self.image2))
        canvas.create_text(self.width/2,  self.height/2,
                           text=self.message, font=font)
        self.resizeAndDrawPics(canvas)

    
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


# textBoxTest()
# testFoodAPI()
testNumpy()
testPIL()
# matplottest()
# matplottest2()


from cmu_112_graphics import *
import random, requests, bs4, json

class PuzzleMode(Mode):
    def appStarted(mode):
        mode.puzzle1 = False
        mode.puzzle2 = False
       #  mode.puzzle1loadingmessage = False

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

    def mousePressed(mode, event):
        if (0 <= event.x <= 200) and (0 <= event.y <= 375): 
            # mode.puzzle1loadingmessage = True
            mode.app.setActiveMode(mode.app.puzzleMode1)
        elif (0 <= event.x <= 200) and (375 < event.y <= 750): 
            mode.app.setActiveMode(mode.app.puzzleMode2)

    def mouseMoved(mode, event):
        if (0 <= event.x <= 200) and (0 <= event.y <= 375): 
            mode.puzzle1 = True
            mode.puzzle2 = False
        elif (0 <= event.x <= 200) and (375 < event.y <= 750): 
            mode.puzzle2 = True
            mode.puzzle1 = False
        else:
            mode.puzzle1 = mode.puzzle2 = False

    def redrawAll(mode, canvas):
        canvas.create_line(200, 0, 200, mode.height)
        # If I feel like making 3 puzzle modes     
        # canvas.create_rectangle(0, 0, 200, 250, fill='red')
        # canvas.create_text(100, 125, text='Puzzle 1', font='Calibri 15 bold')
        # canvas.create_rectangle(0, 250, 200, 500, fill='yellow')
        # canvas.create_text(100, 375, text='Puzzle 2', font='Calibri 15 bold')
        # canvas.create_rectangle(0, 500, 200, 750, fill='green')
        # canvas.create_text(100, 625, text='Puzzle 3', font='Calibri 15 bold')
        canvas.create_rectangle(0, 0, 200, 375, fill='green')
        canvas.create_text(100, 187.5, text='Puzzle 1\nDifficulty: Easy', font='Calibri 15 bold')
        canvas.create_rectangle(0, 375, 200, 750, fill='red')
        canvas.create_text(100, 562.5, text='Puzzle 2\nDifficulty: Hard', font='Calibri 15 bold')
        if mode.puzzle1:
            canvas.create_text(2*mode.width/3, 50, text='Puzzle 1: Highest Calorie Food', font='Calibri 20 bold')
            canvas.create_text(250, mode.height/2 - 200, text='Given a list of foods and\ntheir macronutrient proportions,\nfind the food with the most calories!', font='Calibri 15 bold', anchor='w')
            # CITATION: https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/1200px-Good_Food_Display_-_NCI_Visuals_Online.jpg
            canvas.create_image(2*mode.width/3, 3*mode.height/4 - 100, image=ImageTk.PhotoImage(mode.scaleImage(mode.loadImage('foodspic.jpg'), 0.35)))
        elif mode.puzzle2:
            canvas.create_text(2*mode.width/3, 50, text='Puzzle 2: Food Choice Optimization', font='Calibri 20 bold')
            canvas.create_text(250, mode.height/2-200, text='Given a restaurant menu of\nfoods + prices and a spending limit,\nfind a combination of food that will\nbe the most fulfilling in calories!', font='Calibri 15 bold', anchor='w')
            # CITATION: https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/117520118/original/97b74413d19313b1d51958209e87e414a4ba3719/design-restaurant-menu-menu-design-food-menu-price-list-menu-catalog-pdf-flyer.jpg
            canvas.create_image(2*mode.width/3, 3*mode.height/4 - 100, image=ImageTk.PhotoImage(mode.scaleImage(mode.loadImage('restaurantmenupic.jpg'), 0.25)))
        if not (mode.puzzle1 or mode.puzzle2):
            canvas.create_text(2*mode.width/3, mode.height/2 - 200, text='Hover over one of\nthe puzzle choices\nto see what they are!', font='Calibri 20 bold')
            canvas.create_text(2*mode.width/3, mode.height/2 + 200, text='Click one of them\nwhen you are ready\nto play and learn!', font='Calibri 20 bold')
        # if mode.puzzle1loadingmessage:
        #     canvas.create_text(mode.width/2, 700, text='Loading...', font='Calibri 15 bold')

# Puzzle 1: Highest Calorie Food
class PuzzleMode1(PuzzleMode):
    randomizedFoodList = []
    doOnceCounter = 0
    calorieCounts = []
    selectedItem = None
    foodselected = False
    answerBoxColor = 'yellow'
    answerResponse = False

    def appStarted(mode):
        # pull random foods from API
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.puzzleMode) 
    
    def mousePressed(mode, event):
        if (575 <= event.x <= 650):
            # CITATION: https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
            if (120 <= event.y <= 135): # 100
                PuzzleMode1.selectedItem = PuzzleMode1.randomizedFoodList[0][0]
                mode.foodselected = True
            elif (195 <= event.y <= 210): # 175
                PuzzleMode1.selectedItem = PuzzleMode1.randomizedFoodList[1][0]
                mode.foodselected = True
            elif (270 <= event.y <= 285): # 250
                PuzzleMode1.selectedItem = PuzzleMode1.randomizedFoodList[2][0]
                mode.foodselected = True
            elif (345 <= event.y <= 360): # 325
                PuzzleMode1.selectedItem = PuzzleMode1.randomizedFoodList[3][0]
                mode.foodselected = True
            elif (420 <= event.y <= 435): # 400
                PuzzleMode1.selectedItem = PuzzleMode1.randomizedFoodList[4][0]
                mode.foodselected = True
            elif (495 <= event.y <= 510): # 475
                PuzzleMode1.selectedItem = PuzzleMode1.randomizedFoodList[5][0]
                mode.foodselected = True
            elif (570 <= event.y <= 585): # 550
                PuzzleMode1.selectedItem = PuzzleMode1.randomizedFoodList[6][0]
                mode.foodselected = True
            elif (645 <= event.y <= 660): # 625
                PuzzleMode1.selectedItem = PuzzleMode1.randomizedFoodList[7][0]
                mode.foodselected = True
            PuzzleMode1.answerBoxColor = 'yellow'
            PuzzleMode1.answerResponse = False
        if (550 <= event.x <= 650) and (700 <= event.y <= 750): # 550, 700, 650, 750
            PuzzleMode1.answerResponse = True
            print(PuzzleMode1.randomizedFoodList)
            if PuzzleMode1.selectedItem == PuzzleMode1.randomizedFoodList[mode.highestCalorieFood][0]:
                PuzzleMode1.answerBoxColor = 'green'
            else:
                PuzzleMode1.answerBoxColor = 'red'

        if (400 <= event.x <= 500) and (700 <= event.y <= 750): # 400, 700, 500, 750
            PuzzleMode1.randomizedFoodList = []
            PuzzleMode1.calorieCounts = []
            PuzzleMode1.doOnceCounter = 0
            PuzzleMode1.answerBoxColor = 'yellow'
            PuzzleMode1.answerResponse = False
    
    def mouseMoved(mode, event):
        pass

    def getCachedPhotoImage(mode, image):
        # stores a cached version of the PhotoImage in the PIL/Pillow image
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def displayFoods(mode, canvas):
        if mode.foodentered:
            for i in range(len(PuzzleMode1.randomizedFoodList)):
                # cache the image
                resizedImage = mode.scaleImage(mode.loadImage(PuzzleMode1.randomizedFoodList[i][1][1]), 0.5)
                cachedResizedImage = mode.getCachedPhotoImage(resizedImage)
                # create the cached image
                canvas.create_image(250, PuzzleMode1.randomizedFoodList[i][2], image=cachedResizedImage)
                # display food name and macro counts
                canvas.create_text(300, PuzzleMode1.randomizedFoodList[i][2] - 10, text=PuzzleMode1.randomizedFoodList[i][0], font='Calibri 13 bold',anchor='w')
                canvas.create_text(300, PuzzleMode1.randomizedFoodList[i][2] + 10, text=f'Carbs (g): {PuzzleMode1.randomizedFoodList[i][1][0][0]}', anchor='w')
                canvas.create_text(400, PuzzleMode1.randomizedFoodList[i][2] + 10, text=f'Protein (g): {PuzzleMode1.randomizedFoodList[i][1][0][1]}', anchor='w')
                canvas.create_text(500, PuzzleMode1.randomizedFoodList[i][2] + 10, text=f'Fat (g): {PuzzleMode1.randomizedFoodList[i][1][0][2]}', anchor='w')
                # separate foods with lines
                canvas.create_line(200, PuzzleMode1.randomizedFoodList[i][2] + 37.5, mode.width, PuzzleMode1.randomizedFoodList[i][2] + 37.5)
                # add-to-list button
                canvas.create_rectangle(575, PuzzleMode1.randomizedFoodList[i][2] + 20, 650, PuzzleMode1.randomizedFoodList[i][2] + 35, fill='cyan')
                canvas.create_text(612.5, PuzzleMode1.randomizedFoodList[i][2] + 27.5, text='Select')

    def getFood(mode):
        if PuzzleMode1.doOnceCounter == 0:
            # CITATION: https://stackoverflow.com/questions/37153472/how-to-pick-one-key-from-a-dictionary-randomly
            mode.randomFoods = ['apple', 'orange', 'cheerios', 'chicken', 'nuts', 'fruit', 'turkey', 'yogurt']
            picCy = 100
            for userinput in mode.randomFoods:
                mode.getFoodDict(userinput)
                randomfood = random.choice(list(mode.foodFullDict))
                randomfoodinfo = mode.foodFullDict[randomfood]
                PuzzleMode1.randomizedFoodList.append([randomfood, randomfoodinfo, picCy])
                PuzzleMode1.calorieCounts.append(randomfoodinfo[0][3])
                picCy += 75
                # print(randomfood)
            PuzzleMode1.doOnceCounter = 1
            # print(PuzzleMode1.randomizedFoodList)
            # print(PuzzleMode1.calorieCounts)
            # print(max(PuzzleMode1.calorieCounts))
            mode.highestCalorieFood = (PuzzleMode1.calorieCounts.index(max(PuzzleMode1.calorieCounts)))
            print(mode.highestCalorieFood)
            # print(mode.highestCalorieFood)
            # print(PuzzleMode1.randomizedFoodList[mode.highestCalorieFood][0])
    
    def getFoodDict(mode, userinput):
        # CITATION: https://github.com/USDA/USDA-APIs/issues/64
        # pulling food data from the API
        params = {'api_key': 'xva7eCmcY6On4IRr0o28hpJJLJpQXC1nYebWx4Wa'}
        data = {'generalSearchInput': userinput}
        response = requests.post(
            r'https://api.nal.usda.gov/fdc/v1/foods/search',
            params = params,
            json = data
        )

        mode.foodentered = True
        mode.foodFullDict = dict()
        mode.foodFullDictCoords = dict()
        # create a set to prevent duplicates from showing up
        num = 0
        foodset = set()
        # return top 10 results max using try except so list can be len(10-)
        try:
            while len(foodset) < 4:
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
                # mode.foodFullDict[foodname] = (proteinContent, fatContent, carbContent)
                calories = carbContent * 4 + proteinContent * 4 + fatContent * 9
                mode.foodFullDict[foodname] = (carbContent, proteinContent, fatContent, calories)

        except IndexError:
            pass

        # CITATION: https://stackoverflow.com/questions/21530274/format-for-a-url-that-goes-to-google-image-search
        # web scrape for the image
        picCy = 25 # embed the locations of where they will be placed using picCy
        for foodname in foodset:
            imagerequest = requests.get(f'https://www.google.com/search?tbm=isch&q={foodname}%20food%20or%20drink')
            soup = bs4.BeautifulSoup(imagerequest.text, 'html.parser')
            firstimage = soup.find_all("img")[1]
            firstimage = str(firstimage)
            srcindex = firstimage.find('http')      # parsing for start of link
            foodimageurl = firstimage[srcindex:-3]  # slicing for url of image   
            mode.foodFullDict[foodname] = [mode.foodFullDict[foodname], firstimage[srcindex:-3], picCy] # assign value to key
            mode.foodFullDictCoords[foodname] = picCy
            picCy += 75    

        # print(mode.foodFullDict) # final food dict with macros + image url
    
    def redrawAll(mode, canvas):
        canvas.create_text(mode.width/2, 25, text='Puzzle 1: Highest Calorie Food', font='Calibri 20 bold') # puzzle mode 1 at the top
        canvas.create_text(mode.width/2, 50, text='Given a list of foods and their macronutrient proportions, find the food with the most calories!', font='Calibri 10 bold') # RULES
        canvas.create_rectangle(550, 700, 650, 750, fill='cyan') # check answer button
        canvas.create_text(600, 725, text='Check Answer', font='Calibri 12 bold')
        canvas.create_rectangle(400, 700, 500, 750, fill='cyan') # reset/new puzzle button
        canvas.create_text(450, 725, text='New Puzzle', font='Calibri 12 bold')
        canvas.create_rectangle(0, 75, 200, 750, fill=PuzzleMode1.answerBoxColor)
        mode.getFood()
        mode.displayFoods(canvas)
        if mode.foodselected:
            canvas.create_text(10, mode.height/2 - 100, text='Selected Answer:', font='Calibri 15', anchor='w')
            canvas.create_text(10, mode.height/2 - 80, text=f'{PuzzleMode1.selectedItem[:20]}', font='Calibri 15 bold', anchor='w')
        if PuzzleMode1.answerResponse:
            if PuzzleMode1.answerBoxColor == 'green':
                canvas.create_text(10, mode.height/2 + 100, text='That is correct.\nNice job!', font='Calibri 15 bold', anchor='w')
            else:
                canvas.create_text(10, mode.height/2 + 100, text='Nope, try again.', font='Calibri 15 bold', anchor='w')

# Puzzle 2: Food Choice Optimization (LINEAR PROGRAMMING)
class PuzzleMode2(PuzzleMode):
    def appStarted(mode):
        url = 'https://i.pinimg.com/originals/fe/f7/2f/fef72f73f4f961b4ed6f8e4bb093eb1b.jpg'
        mode.appIcon = mode.loadImage(url)
        mode.appIcon2 = mode.scaleImage(mode.appIcon, 4.5/10)
        filename1 = 'chickfilalogo.png' # CITATION: https://myareanetwork-photos.s3.amazonaws.com/bizlist_photos/t/268981_1526986225.png
        mode.chickfilaImage = mode.loadImage(filename1)
        mode.chickfilaImage2 = mode.scaleImage(mode.chickfilaImage, 1)
        filename2 = 'mcdonaldslogo.jpg' # CITATION: https://www.visitdanvillearea.com/wp-content/uploads/2015/08/McDonalds-Logo-square.jpg
        mode.mcdonaldsImage = mode.loadImage(filename2)
        mode.mcdonaldsImage2 = mode.scaleImage(mode.mcdonaldsImage, 0.95)

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.puzzleMode) 

    def mousePressed(mode, event):
        if ((mode.width/4 - 75 <= event.x <= mode.width/4 + 75) and (35 <= event.y <= 65)) or ((mode.width/4 - 100 <= event.x <= mode.width/4 + 100) and (670 <= event.y <= 700)): mode.app.setActiveMode(mode.app.chickfilaMenu)
        elif ((3*mode.width/4 - 75 <= event.x <= 3*mode.width/4 + 75) and (35 <= event.y <= 65)) or ((3*mode.width/4 - 100 <= event.x <= 3*mode.width/4 + 100) and (670 <= event.y <= 700)): mode.app.setActiveMode(mode.app.mcdonaldsMenu)

    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2, image=ImageTk.PhotoImage(mode.appIcon2))
        canvas.create_text(mode.width/2, 25, text='Puzzle 2: Food Choice Optimization', font='Calibri 20 bold') # puzzle mode 2 at the top
        canvas.create_text(mode.width/2, 50, text='Given a restaurant menu, pick the combo of foods with the most calories, while under a spending limit and other constraints!', font='Calibri 9 bold') # RULES
        # mcdonalds, CHICK-FIL-A logos
        canvas.create_image(mode.width/4, mode.height/2 - 100, image=ImageTk.PhotoImage(mode.chickfilaImage2)) 
        canvas.create_image(3*mode.width/4, mode.height/2 - 100, image=ImageTk.PhotoImage(mode.mcdonaldsImage2)) 

        # CITATION: https://www.chick-fil-a.com/about/who-we-are#:~:text=%E2%80%9CTo%20glorify%20God%20by%20being,Chick%2Dfil%2DA.%E2%80%9D
        canvas.create_text(mode.width/4, 3*mode.height/4,   text='"To glorify God by being a faithful steward\nof all that is entrusted to us and\nto have a positive influence on all\nwho come into contact with Chick-fil-A."', font='Calibri 12 bold')
        # CITATION: https://www.grubstreet.com/2016/03/new-mcdonalds-slogan.html#:~:text=At%20least%20the%20Golden%20Arches,how%20on%20earth%20it's%20pronounced.
        canvas.create_text(3*mode.width/4, 3*mode.height/4, text="\"I'm Lovin' It\"", font='Calibri 12 bold') 

        canvas.create_rectangle(mode.width/4 - 100, 670, mode.width/4 + 100, 700, fill='white')
        canvas.create_rectangle(3*mode.width/4 - 100, 670, 3*mode.width/4 + 100, 700, fill='white')
        canvas.create_text(mode.width/4, 685, text='Use Chick-fil-A Menu', font='Calibri 15 bold')
        canvas.create_text(3*mode.width/4, 685, text="Use McDonald's Menu", font='Calibri 15 bold')

# Plan moving forward:
'''
1.  Puzzle Objective: Maximize calories, while having constraints on cost, certain macro/micro nutrients, and amounts.
2.  Puzzle Objective: Solve for quantities of foods
3.  Steps: Create a dictionary of foods and their calories, cost, and some macro/micros.
4.  Steps: Create an objective function for calories (being maximized) and hardcode slack form in 2D list [ [ ], [ ], [ ], [ ] ]
5.  Steps: Create a constraint on cost (quantity * food price) --> (total - quantity*foodprice - quantity*foodprice - quantity*foodprice, etc.)
6.  Steps: Create a constraint on amounts (no greater than 5?) 
7.  Steps: Create non negative constraints for all variables
8.  Steps: Create multiple equations for restrictions on fat/protein/carbs (40 - (fat content of big mac) * quantity - (fat content of french fries) * quantity, etc.)
9.  Algorithm: Use pivoting to solve for the max of the objective function, find tightest constraint, and replace and check for positive coefficients
10. Algorithm: Iterate through the coefficients until no positive coefficients left (maximum obtained)
'''
class ChickFilA(PuzzleMode2):
    def appStarted(mode):
        pass
    
    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.puzzleMode2)

    def redrawAll(mode, canvas):
        # CITATION: https://www.chick-fil-a.com/about/who-we-are#:~:text=%E2%80%9CTo%20glorify%20God%20by%20being,Chick%2Dfil%2DA.%E2%80%9D
        canvas.create_text(mode.width/2, 25, text='Chick-fil-A Menu', font='Calibri 20 bold') # restaurant name
        canvas.create_text(mode.width/2, 50, text='"To glorify God by being a faithful steward of all that is entrusted to us and to have a positive influence on all who come into contact with Chick-fil-A."', font='Calibri 7 bold') # slogan

class McDonalds(PuzzleMode2):
    def appStarted(mode):
        pass
    
    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.puzzleMode2)
    
    def redrawAll(mode, canvas):
        # CITATION: https://www-beta.mcdonaldsbread.com/en-us/food-values/who-we-are.html
        canvas.create_text(mode.width/2, 25, text="McDonald's Menu", font='Calibri 20 bold') # restaurant name
        canvas.create_text(mode.width/2, 50, text="\"I'm Lovin' It\"", font='Calibri 7 bold') # slogan

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
6.  Steps: Create a constraint on fat and protein
7.  Steps: Create non negative constraints for all variables
8.  Steps: Create multiple equations for restrictions on fat/protein/carbs (40 - (fat content of big mac) * quantity - (fat content of french fries) * quantity, etc.)
9.  Algorithm: Use pivoting to solve for the max of the objective function, find tightest constraint, and replace and check for positive coefficients
10. Algorithm: Iterate through the coefficients until no positive coefficients left (maximum obtained)
'''
class ChickFilA(PuzzleMode2):
    solution = []
    def appStarted(mode):
        mode.totalFat = random.randrange(50, 80, 5)
        mode.totalProtein = random.randrange(30, 60, 5)
        mode.totalCost = random.randrange(20, 50, 5)
        # CITATION: https://www.fastfoodmenuprices.com/chick-fil-a-nutrition/
        # CITATION: https://www.fastfoodmenuprices.com/chick-fil-a-prices/
        mode.chickfila_smallfoods = {   'Hash Browns': [240, -16, -2, -0.99, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0009_%5BFeed%5D_0000s_0028_Breakfast_Hashbrowns_2.png'],
                                        'Icedream® Cone': [170, -4, -5, -1.25, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Drinks/Drinks%20PDP/_0000s_0027_%5BFeed%5D_0006s_0013_Drinks_Ice-Dream.png'],
                                        'Grilled Nuggets': [140, -3.5, -25, -3.75, 'https://www.cfacdn.com/img/order/menu/Online/Entrees/grilledNuggets_8ct_PDP.png'],
                                        '1% White Milk': [90, -2, -7, -1.19, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Drinks/Drinks%20PDP/_0000s_0020_%5BFeed%5D_0006s_0019_Drinks_Milk.png'] }
        mode.chickfila_bigfoods = {     'Chick-fil-A® Chicken Biscuit': [450, -21, -17, -2.19, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20Desktop/_0000s_0000_Stack620_0000_CFA_1605_60_Biscuit_Chicken_PROD_2155_1240px.png'],
                                        'Chick-n-Strips™': [350, -17, -28, -3.05, 'https://www.cfacdn.com/img/order/menu/Online/Entrees/strips_3ct_PDP.png'],
                                        'Cobb Salad': [510, -27, -40, -7.19, 'https://www.cfacdn.com/img/order/menu/Online/Salads%26wraps/cobbSalad_nug_pdp.png'],
                                        'Bacon, Egg & Cheese Biscuit': [420, -21, -15, -2.59, 'https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20Desktop/_0000s_0008_Bacon-Egg-Cheese-Biscuit_620_PDP.png'] }
        mode.fooditem1name = random.choice(list(mode.chickfila_bigfoods))
        mode.fooditem2name = random.choice(list(mode.chickfila_smallfoods))
        mode.fooditem3name = random.choice(list(mode.chickfila_smallfoods))
        while mode.fooditem2name == mode.fooditem3name:
            mode.fooditem3name = random.choice(list(mode.chickfila_smallfoods))
        print(mode.fooditem1name, mode.fooditem2name, mode.fooditem3name)
        mode.fooditem1 = mode.chickfila_bigfoods[mode.fooditem1name]
        mode.fooditem2 = mode.chickfila_smallfoods[mode.fooditem2name]
        mode.fooditem3 = mode.chickfila_smallfoods[mode.fooditem3name]
        print(mode.fooditem1, mode.fooditem2, mode.fooditem3)
        mode.simplexAlgorithm()
        mode.userFat = mode.userProtein = mode.userCalories = mode.userCost = 0
        mode.food1Quantity = mode.food2Quantity = mode.food3Quantity = 0
        mode.mean_squared_error = 8888
        mode.showsolution = False
    
    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.puzzleMode2)
    
    def simplexAlgorithm(mode):
        mode.totalCalories =    0
        solution =         [0, 0, 0, mode.totalFat, mode.totalProtein, mode.totalCost]

        tightestConstraintA = tightestConstraintB = tightestConstraintC = None

        # more simplified labels for slackForm system
        #                calories      fat           protein       cost
        a0, a1, a2, a3 = mode.fooditem1[0], mode.fooditem1[1], mode.fooditem1[2], mode.fooditem1[3] # 'Chick-fil-A® Chicken Biscuit' (a)
        b0, b1, b2, b3 = mode.fooditem2[0], mode.fooditem2[1], mode.fooditem2[2], mode.fooditem2[3] # 'Hash Browns'                  (b)
        c0, c1, c2, c3 = mode.fooditem3[0], mode.fooditem3[1], mode.fooditem3[2], mode.fooditem3[3] # 'Icedream® Cone'               (c)

        # slackForm linear system, objective function is slackForm[0], to be maximized
        #             constant       a   b   c    d   e   f
        slackForm = [[mode.totalCalories, a0, b0, c0,  0,  0,  0], # calories equation
                    [mode.totalFat,      a1, b1, c1, -1,  0,  0], # fat equation
                    [mode.totalProtein,  a2, b2, c2,  0, -1,  0], # protein equation
                    [mode.totalCost,     a3, b3, c3,  0,  0, -1]] # cost equation

        # if coefficient of a is positive, maximum can still be achieved; thus, find biggest constraint on a
        if slackForm[0][1] >= 0:
            
            # finding tightest constraint
            listOfConstraints = []
            listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][1])) # slackForm[1][1]
            listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][1])) # slackForm[2][1]
            listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][1])) # slackForm[3][1]
            tightestConstraint = min(listOfConstraints)
            # print("List of constraints:", listOfConstraints) # fat, protein, cost
            # print("The tightest constraint is:", tightestConstraint) 

            # find the equation where the tightest constraint was found
            tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
            # print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
            tightestConstraintA = tightestConstraintEquation

            slackForm[tightestConstraintEquation][1] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
            # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
            newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][1], # constant
                        1,                                                                                   # a
                        slackForm[tightestConstraintEquation][2] / slackForm[tightestConstraintEquation][1], # b
                        slackForm[tightestConstraintEquation][3] / slackForm[tightestConstraintEquation][1], # c
                        slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][1], # d
                        slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][1], # e 
                        slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][1]] # f
            # print("The rearranged equation is:", newEquation) # this is the rearranged equation

            slackForm2 = [  [slackForm[0][0] + slackForm[0][1] * newEquation[0], 0, slackForm[0][2] + slackForm[0][1] * newEquation[2], slackForm[0][3] + slackForm[0][1] * newEquation[3],  slackForm[0][4] + slackForm[0][1] * newEquation[4],  slackForm[0][5] + slackForm[0][1] * newEquation[5],  slackForm[0][6] + slackForm[0][1] * newEquation[6]], # calories equation
                            [slackForm[1][0] + slackForm[1][1] * newEquation[0], 0, slackForm[1][2] + slackForm[1][1] * newEquation[2], slackForm[1][3] + slackForm[1][1] * newEquation[3],  slackForm[1][4] + slackForm[1][1] * newEquation[4],  slackForm[1][5] + slackForm[1][1] * newEquation[5],  slackForm[1][6] + slackForm[1][1] * newEquation[6]], # fat equation
                            [slackForm[2][0] + slackForm[2][1] * newEquation[0], 0, slackForm[2][2] + slackForm[2][1] * newEquation[2], slackForm[2][3] + slackForm[2][1] * newEquation[3],  slackForm[2][4] + slackForm[2][1] * newEquation[4],  slackForm[2][5] + slackForm[2][1] * newEquation[5],  slackForm[2][6] + slackForm[2][1] * newEquation[6]], # protein equation
                            [slackForm[3][0] + slackForm[3][1] * newEquation[0], 0, slackForm[3][2] + slackForm[3][1] * newEquation[2], slackForm[3][3] + slackForm[3][1] * newEquation[3],  slackForm[3][4] + slackForm[3][1] * newEquation[4],  slackForm[3][5] + slackForm[3][1] * newEquation[5],  slackForm[3][6] + slackForm[3][1] * newEquation[6]]] # cost equation

            slackForm2[tightestConstraintEquation] = newEquation
            slackForm2[tightestConstraintEquation][1] = -1

            # print(slackForm2[0])
            # print(slackForm2[1])
            # print(slackForm2[2])
            # print(slackForm2[3])
            slackForm = slackForm2
            solution[0] = slackForm[tightestConstraintEquation][0]
            # print("Current solution is:", solution)
            # print(slackForm)
        
        # if coefficient of b is positive, maximum can still be achieved; thus, find biggest constraint on b
        if slackForm[0][2] >= 0:

            # finding tightest constraint
            listOfConstraints = []
            listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][2])) # slackForm[1][1]
            listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][2])) # slackForm[2][1]
            listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][2])) # slackForm[3][1]
            tightestConstraint = min(listOfConstraints)
            # print("List of constraints:", listOfConstraints) # fat, protein, cost
            # print("The tightest constraint is:", tightestConstraint) 

            # find the equation where the tighest constraint was found
            tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
            # print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
            tightestConstraintB = tightestConstraintEquation

            slackForm[tightestConstraintEquation][2] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
            # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
            newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][2], # constant
                        slackForm[tightestConstraintEquation][1] / slackForm[tightestConstraintEquation][2], # a
                        1,                                                                                   # b
                        slackForm[tightestConstraintEquation][3] / slackForm[tightestConstraintEquation][2], # c
                        slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][2], # d
                        slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][2], # e 
                        slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][2]] # f
            # print("The rearranged equation is:", newEquation) # this is the rearranged equation

            slackForm2 = [  [slackForm[0][0] + slackForm[0][2] * newEquation[0], slackForm[0][1] + slackForm[0][2] * newEquation[1], 0, slackForm[0][3] + slackForm[0][2] * newEquation[3],  slackForm[0][4] + slackForm[0][2] * newEquation[4],  slackForm[0][5] + slackForm[0][2] * newEquation[5],  slackForm[0][6] + slackForm[0][2] * newEquation[6]], # calories equation
                            [slackForm[1][0] + slackForm[1][2] * newEquation[0], slackForm[1][1] + slackForm[1][2] * newEquation[1], 0, slackForm[1][3] + slackForm[1][2] * newEquation[3],  slackForm[1][4] + slackForm[1][2] * newEquation[4],  slackForm[1][5] + slackForm[1][2] * newEquation[5],  slackForm[1][6] + slackForm[1][2] * newEquation[6]], # fat equation
                            [slackForm[2][0] + slackForm[2][2] * newEquation[0], slackForm[2][1] + slackForm[2][2] * newEquation[1], 0, slackForm[2][3] + slackForm[2][2] * newEquation[3],  slackForm[2][4] + slackForm[2][2] * newEquation[4],  slackForm[2][5] + slackForm[2][2] * newEquation[5],  slackForm[2][6] + slackForm[2][2] * newEquation[6]], # protein equation
                            [slackForm[3][0] + slackForm[3][2] * newEquation[0], slackForm[3][1] + slackForm[3][2] * newEquation[1], 0, slackForm[3][3] + slackForm[3][2] * newEquation[3],  slackForm[3][4] + slackForm[3][2] * newEquation[4],  slackForm[3][5] + slackForm[3][2] * newEquation[5],  slackForm[3][6] + slackForm[3][2] * newEquation[6]]] # cost equation

            slackForm2[tightestConstraintEquation] = newEquation
            slackForm2[tightestConstraintEquation][2] = -1
            

            # print(slackForm2[0])
            # print(slackForm2[1])
            # print(slackForm2[2])
            # print(slackForm2[3])
            
            slackForm = slackForm2
            solution[0] = slackForm[tightestConstraintA][0]
            solution[1] = slackForm[tightestConstraintEquation][0]
            tightestConstraintB = tightestConstraintEquation
            # print(slackForm)
            if tightestConstraintB == tightestConstraintA: solution[0] = 0

        # if coefficient of c is positive, maximum can still be achieved; thus, find biggest constraint on c
        if slackForm[0][3] >= 0:

            # finding tightest constraint
            listOfConstraints = []
            listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][3])) # slackForm[1][1]
            listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][3])) # slackForm[2][1]
            listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][3])) # slackForm[3][1]
            tightestConstraint = min(listOfConstraints)
            # print("List of constraints:", listOfConstraints) # fat, protein, cost
            # print("The tightest constraint is:", tightestConstraint) 

            # find the equation where the tighest constraint was found
            tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
            # print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
            tightestConstraintC = tightestConstraintEquation

            slackForm[tightestConstraintEquation][3] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
            # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
            newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][3], # constant
                        slackForm[tightestConstraintEquation][1] / slackForm[tightestConstraintEquation][3], # a
                        slackForm[tightestConstraintEquation][2] / slackForm[tightestConstraintEquation][3], # b
                        1,                                                                                   # c
                        slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][3], # d
                        slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][3], # e 
                        slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][3]] # f
            # print("The rearranged equation is:", newEquation) # this is the rearranged equation

            slackForm2 = [  [slackForm[0][0] + slackForm[0][3] * newEquation[0], slackForm[0][1] + slackForm[0][3] * newEquation[1], slackForm[0][3] + slackForm[0][3] * newEquation[2], 0,  slackForm[0][4] + slackForm[0][3] * newEquation[4],  slackForm[0][5] + slackForm[0][3] * newEquation[5],  slackForm[0][6] + slackForm[0][3] * newEquation[6]], # calories equation
                            [slackForm[1][0] + slackForm[1][3] * newEquation[0], slackForm[1][1] + slackForm[1][3] * newEquation[1], slackForm[1][3] + slackForm[1][3] * newEquation[2], 0,  slackForm[1][4] + slackForm[1][3] * newEquation[4],  slackForm[1][5] + slackForm[1][3] * newEquation[5],  slackForm[1][6] + slackForm[1][3] * newEquation[6]], # fat equation
                            [slackForm[2][0] + slackForm[2][3] * newEquation[0], slackForm[2][1] + slackForm[2][3] * newEquation[1], slackForm[2][3] + slackForm[2][3] * newEquation[2], 0,  slackForm[2][4] + slackForm[2][3] * newEquation[4],  slackForm[2][5] + slackForm[2][3] * newEquation[5],  slackForm[2][6] + slackForm[2][3] * newEquation[6]], # protein equation
                            [slackForm[3][0] + slackForm[3][3] * newEquation[0], slackForm[3][1] + slackForm[3][3] * newEquation[1], slackForm[3][3] + slackForm[3][3] * newEquation[2], 0,  slackForm[3][4] + slackForm[3][3] * newEquation[4],  slackForm[3][5] + slackForm[3][3] * newEquation[5],  slackForm[3][6] + slackForm[3][3] * newEquation[6]]] # cost equation

            slackForm2[tightestConstraintEquation] = newEquation
            slackForm2[tightestConstraintEquation][3] = -1

            # print(slackForm2[0])
            # print(slackForm2[1])
            # print(slackForm2[2])
            # print(slackForm2[3])
            slackForm = slackForm2
            solution[0] = slackForm[tightestConstraintA][0]
            if tightestConstraintB != None:
                solution[1] = slackForm[tightestConstraintB][0]
            if tightestConstraintC != None:
                solution[2] = slackForm[tightestConstraintEquation][0]
            # print(slackForm)
            if tightestConstraintC == tightestConstraintA: solution[0] = 0
            if tightestConstraintC == tightestConstraintB: solution[1] = 0

        totalCalories = slackForm[0][0]
        ChickFilA.solution = solution
        print("FINAL SOLUTION:", solution)
        print("TOTAL CALORIES:", totalCalories)

    def getCachedPhotoImage(mode, image):
        # stores a cached version of the PhotoImage in the PIL/Pillow image
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def displayFoods(mode, canvas):
        resizedImage1 = mode.scaleImage(mode.loadImage(mode.fooditem1[4]), 0.15)
        cachedResizedImage1 = mode.getCachedPhotoImage(resizedImage1)
        canvas.create_image(100, 200, image=cachedResizedImage1)
        canvas.create_text(200, 200 - 10, text=f'{mode.fooditem1name} | Price: ${abs(mode.fooditem1[3])}', anchor='w', font='Calibri 15 bold')
        canvas.create_text(200, 200 + 10, text=f'Calories: {abs(mode.fooditem1[0])} cals | Fat: {abs(mode.fooditem1[1])}g | Protein: {abs(mode.fooditem1[2])}g', anchor='w')
        resizedImage2 = mode.scaleImage(mode.loadImage(mode.fooditem2[4]), 0.15)
        cachedResizedImage2 = mode.getCachedPhotoImage(resizedImage2)
        canvas.create_image(100, 350, image=cachedResizedImage2)
        canvas.create_text(200, 350 - 10, text=f'{mode.fooditem2name} | Price: ${abs(mode.fooditem2[3])}', anchor='w', font='Calibri 15 bold')
        canvas.create_text(200, 350 + 10, text=f'Calories: {abs(mode.fooditem2[0])} cals | Fat: {abs(mode.fooditem2[1])}g | Protein: {abs(mode.fooditem2[2])}g', anchor='w')
        resizedImage3 = mode.scaleImage(mode.loadImage(mode.fooditem3[4]), 0.15)
        cachedResizedImage3 = mode.getCachedPhotoImage(resizedImage3)
        canvas.create_image(100, 500, image=cachedResizedImage3)
        canvas.create_text(200, 500 - 10, text=f'{mode.fooditem3name} | Price: ${abs(mode.fooditem3[3])}', anchor='w', font='Calibri 15 bold')
        canvas.create_text(200, 500 + 10, text=f'Calories: {abs(mode.fooditem3[0])} cals | Fat: {abs(mode.fooditem3[1])}g | Protein: {abs(mode.fooditem3[2])}g', anchor='w')

    def mousePressed(mode, event):
        if (mode.width/2 - 100 <= event.x <= mode.width/2 + 100) and (mode.height - 50 <= event.y <= mode.height):
            # check answer and use mean squared error
            mode.fatDifference = ChickFilA.solution[0] - mode.food1Quantity
            mode.proteinDifference = ChickFilA.solution[1] - mode.food2Quantity
            mode.costDifference = ChickFilA.solution[2] - mode.food3Quantity
            print("Differences:", mode.fatDifference, mode.proteinDifference, mode.costDifference)
            mode.mean_squared_error = (mode.fatDifference**2 + mode.proteinDifference**2 + mode.costDifference**2) / 3
            print("SOLUTION:", ChickFilA.solution)
            print("THE MSE IS:", mode.mean_squared_error)
        elif (0 <= event.x <= 100) and (mode.height - 50 <= event.y <= mode.height):
            mode.appStarted()
        elif (550 <= event.x <= 650) and (mode.height - 50 <= event.y <= mode.height):
            mode.showsolution = not mode.showsolution
        elif (500 <= event.x <= 600):
            if (205 <= event.y <= 225): 
                mode.food1Quantity = mode.getUserInput("What quantity? (can be a float, but must be non negative)")
                if mode.food1Quantity != None:
                    mode.quantityReplaced = mode.food1Quantity.replace('.','', 1)
                    while True:
                        if mode.food1Quantity == 0: break
                        elif mode.food1Quantity == None or not mode.quantityReplaced.isdigit() or float(mode.food1Quantity) > 100 or float(mode.food1Quantity) < 0:
                            mode.food1Quantity = mode.getUserInput("How many servings?")
                            if mode.food1Quantity != None:
                                mode.quantityReplaced = mode.food1Quantity.replace('.','', 1)
                        else:
                            mode.food1Quantity = float(mode.food1Quantity)
                            break
                else:
                    mode.food1Quantity = 0
            elif (355 <= event.y <= 375):
                mode.food2Quantity = mode.getUserInput("What quantity? (can be a float, but must be non negative)")
                if mode.food2Quantity != None:
                    mode.quantityReplaced = mode.food2Quantity.replace('.','', 1)
                    while True:
                        if mode.food2Quantity == 0: break
                        elif mode.food2Quantity == None or not mode.quantityReplaced.isdigit() or float(mode.food2Quantity) > 100 or float(mode.food2Quantity) < 0:
                            mode.food2Quantity = mode.getUserInput("How many servings?")
                            if mode.food2Quantity != None:
                                mode.quantityReplaced = mode.food2Quantity.replace('.','', 1)
                        else:
                            mode.food2Quantity = float(mode.food2Quantity)
                            break
                else:
                    mode.food2Quantity = 0
            elif (505 <= event.y <= 525):
                mode.food3Quantity = mode.getUserInput("What quantity? (can be a float, but must be non negative)")
                if mode.food3Quantity != None:
                    mode.quantityReplaced = mode.food3Quantity.replace('.','', 1)
                    while True:
                        if mode.food3Quantity == 0: break
                        elif mode.food3Quantity == None or not mode.quantityReplaced.isdigit() or float(mode.food3Quantity) > 50 or float(mode.food3Quantity) < 0:
                            mode.food3Quantity = mode.getUserInput("How many servings?")
                            if mode.food3Quantity != None:
                                mode.quantityReplaced = mode.food3Quantity.replace('.','', 1)
                        else:
                            mode.food3Quantity = float(mode.food3Quantity)
                            break
                else:
                    mode.food3Quantity = 0
            mode.userCalories = abs(mode.fooditem1[0]) * mode.food1Quantity + abs(mode.fooditem2[0]) * mode.food2Quantity + abs(mode.fooditem3[0]) * mode.food3Quantity
            mode.userFat = abs(mode.fooditem1[1]) * mode.food1Quantity + abs(mode.fooditem2[1]) * mode.food2Quantity + abs(mode.fooditem3[1]) * mode.food3Quantity
            mode.userProtein = abs(mode.fooditem1[2]) * mode.food1Quantity + abs(mode.fooditem2[2]) * mode.food2Quantity + abs(mode.fooditem3[2]) * mode.food3Quantity
            mode.userCost = abs(mode.fooditem1[3]) * mode.food1Quantity + abs(mode.fooditem2[3]) * mode.food2Quantity + abs(mode.fooditem3[3]) * mode.food3Quantity

    def redrawAll(mode, canvas):
        # CITATION: https://www.chick-fil-a.com/about/who-we-are#:~:text=%E2%80%9CTo%20glorify%20God%20by%20being,Chick%2Dfil%2DA.%E2%80%9D
        canvas.create_text(mode.width/2, 25, text='Chick-fil-A Menu', font='Calibri 20 bold') # restaurant name
        canvas.create_text(mode.width/2, 50, text='"To glorify God by being a faithful steward of all that is entrusted to us and to have a positive influence on all who come into contact with Chick-fil-A."', font='Calibri 7 bold') # slogan
        canvas.create_text(mode.width/2, 75, text=f'Objective: maximize total calories, get <={mode.totalFat}g of fat, get <={mode.totalProtein}g of protein, and spend <= ${mode.totalCost}!')
        # canvas.create_text(mode.width/2, 100, text=f'Current Input Results: {mode.userCalories} calories, {mode.userFat}g of fat, {mode.userProtein}g of protein, for ${mode.userCost}')
        canvas.create_text(mode.width/2, 100, text='Current Input Results: %0.2f calories, %0.2fg of fat, %0.2fg of protein, for $%0.2f' % (mode.userCalories, mode.userFat, mode.userProtein, mode.userCost))
        mode.displayFoods(canvas)
        solutiontoggle = 'See Solution'
        if mode.showsolution:
            canvas.create_text(mode.width/2, 625, text='Solution: %0.4f calories, %0.4fg fat, %0.4fg protein, $%0.2f' % (ChickFilA.solution[0], ChickFilA.solution[1], ChickFilA.solution[2], ChickFilA.solution[3]))
            solutiontoggle = 'Close Solution'
        canvas.create_rectangle(0, mode.height - 50, 100, mode.height, fill='cyan')
        canvas.create_text(50, mode.height - 25, text='New Puzzle', font='Calibri 10')
        canvas.create_rectangle(550, mode.height - 50, 650, mode.height, fill='cyan')
        canvas.create_text(600, mode.height - 25, text=solutiontoggle, font='Calibri 10')
        canvas.create_rectangle(500, 200 + 5, 600, 200 + 25, fill='cyan')
        canvas.create_text(550, 215, text='Change Quantity', font='Calibri 10')
        canvas.create_text(550, 235, text='Current Quantity: %0.4f' % mode.food1Quantity, font='Calibri 10')
        canvas.create_rectangle(500, 350 + 5, 600, 350 + 25, fill='cyan')
        canvas.create_text(550, 365, text='Change Quantity', font='Calibri 10')
        canvas.create_text(550, 385, text='Current Quantity: %0.4f' % mode.food2Quantity, font='Calibri 10')
        canvas.create_rectangle(500, 500 + 5, 600, 500 + 25, fill='cyan')
        canvas.create_text(550, 515, text='Change Quantity', font='Calibri 10')
        canvas.create_text(550, 535, text='Current Quantity: %0.4f' % mode.food3Quantity, font='Calibri 10')
        canvas.create_rectangle(mode.width/2 - 100, mode.height - 50, mode.width/2 + 100, mode.height, fill='cyan')
        canvas.create_text(mode.width/2, 725, text='Check Answer', font='Calibri 10')
        canvas.create_text(mode.width/2, 650, text='Mean-Squared Error (how far you are from the optimized solution, 0 is the best score!): %0.4f' % mode.mean_squared_error, font='Calibri 11 bold')
        if mode.mean_squared_error <= 10**(-5): canvas.create_text(mode.width/2 + 160, 725, text='You got it!')

class McDonalds(PuzzleMode2):
    solution = []
    def appStarted(mode):
        mode.totalFat = random.randrange(50, 80, 5)
        mode.totalProtein = random.randrange(30, 60, 5)
        mode.totalCost = random.randrange(20, 50, 5)
        # CITATION: https://www.fastfoodmenuprices.com/mcdonalds-nutrition/
        # CITATION: https://www.fastfoodmenuprices.com/mcdonalds-prices/
        mode.mcdonalds_smallfoods = {   'Hash Brown': [240, -16, -2, -0.99, 'https://www.mcdonalds.com/is/image/content/dam/uk/nfl/nutrition/nfl-product/product/products/mcdonalds-Hash-Brown.jpg'],
                                        'Chicken McNuggets® (6 piece)': [280, -18, -13, -4.49, 'https://www.mcdonalds.com/is/image/content/dam/uk/nfl/nutrition/nfl-product/product/products/mcdonalds-Chicken-McNuggets-6-pieces.jpg'],
                                        'Premium Bacon Ranch Salad': [140, -7, -9, -4.59, 'https://www.mcdonalds.com/content/dam/usa/nfl/nutrition/items/regular/desktop/t-mcdonalds-Premium-Bacon-Ranch-Salad-with-Grilled-Chicken.jpg'],
                                        'Egg McMuffin®': [300, -13, -17, -2.79, 'https://www.mcdonalds.com/is/image/content/dam/usa/nfl/nutrition/items/hero/desktop/t-mcdonalds-Egg-McMuffin.jpg'] }
        mode.mcdonalds_bigfoods = {     'Big Mac': [530, -27, -24, -3.99, 'https://www.mcdonalds.com/is/image/content/dam/uk/nfl/nutrition/nfl-product/product/products/mcdonalds-Big-Mac.jpg'],
                                        'Bacon Clubhouse Burger': [720, -40, -39, -4.49, 'https://i.insider.com/5319eaa669beddb66190cbed?width=429&format=jpeg'],
                                        'Big Breakfast with Hotcakes': [1090, -56, -36, -5.49, 'https://www.mcdonalds.com/is/image/content/dam/usa/nfl/nutrition/items/hero/desktop/t-mcdonalds-Big-Breakfast-with-Hotcakes-Regular-Size-Biscuit.jpg'],
                                        'Premium McWrap Chicken & Ranch': [610, -31, -27, -4.39, 'https://www.mcdonalds.com/content/dam/ca/nfl/web/nutrition/products/tile/en/mcdonalds-chicken-bacon-signature-mcwrap-grilled.jpg'] }
        mode.fooditem1name = random.choice(list(mode.mcdonalds_bigfoods))
        mode.fooditem2name = random.choice(list(mode.mcdonalds_smallfoods))
        mode.fooditem3name = random.choice(list(mode.mcdonalds_smallfoods))
        while mode.fooditem2name == mode.fooditem3name:
            mode.fooditem3name = random.choice(list(mode.mcdonalds_smallfoods))
        print(mode.fooditem1name, mode.fooditem2name, mode.fooditem3name)
        mode.fooditem1 = mode.mcdonalds_bigfoods[mode.fooditem1name]
        mode.fooditem2 = mode.mcdonalds_smallfoods[mode.fooditem2name]
        mode.fooditem3 = mode.mcdonalds_smallfoods[mode.fooditem3name]
        print(mode.fooditem1, mode.fooditem2, mode.fooditem3)
        mode.simplexAlgorithm()
        mode.userFat = mode.userProtein = mode.userCalories = mode.userCost = 0
        mode.food1Quantity = mode.food2Quantity = mode.food3Quantity = 0
        mode.mean_squared_error = 8888
        mode.showsolution = False
    
    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.puzzleMode2)
    
    def simplexAlgorithm(mode):
        mode.totalCalories =    0
        solution =         [0, 0, 0, mode.totalFat, mode.totalProtein, mode.totalCost]

        tightestConstraintA = tightestConstraintB = tightestConstraintC = None

        # more simplified labels for slackForm system
        #                calories      fat           protein       cost
        a0, a1, a2, a3 = mode.fooditem1[0], mode.fooditem1[1], mode.fooditem1[2], mode.fooditem1[3] # 'Chick-fil-A® Chicken Biscuit' (a)
        b0, b1, b2, b3 = mode.fooditem2[0], mode.fooditem2[1], mode.fooditem2[2], mode.fooditem2[3] # 'Hash Browns'                  (b)
        c0, c1, c2, c3 = mode.fooditem3[0], mode.fooditem3[1], mode.fooditem3[2], mode.fooditem3[3] # 'Icedream® Cone'               (c)

        # slackForm linear system, objective function is slackForm[0], to be maximized
        #             constant       a   b   c    d   e   f
        slackForm = [[mode.totalCalories, a0, b0, c0,  0,  0,  0], # calories equation
                    [mode.totalFat,      a1, b1, c1, -1,  0,  0], # fat equation
                    [mode.totalProtein,  a2, b2, c2,  0, -1,  0], # protein equation
                    [mode.totalCost,     a3, b3, c3,  0,  0, -1]] # cost equation

        # if coefficient of a is positive, maximum can still be achieved; thus, find biggest constraint on a
        if slackForm[0][1] >= 0:
            
            # finding tightest constraint
            listOfConstraints = []
            listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][1])) # slackForm[1][1]
            listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][1])) # slackForm[2][1]
            listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][1])) # slackForm[3][1]
            tightestConstraint = min(listOfConstraints)
            # print("List of constraints:", listOfConstraints) # fat, protein, cost
            # print("The tightest constraint is:", tightestConstraint) 

            # find the equation where the tightest constraint was found
            tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
            # print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
            tightestConstraintA = tightestConstraintEquation

            slackForm[tightestConstraintEquation][1] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
            # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
            newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][1], # constant
                        1,                                                                                   # a
                        slackForm[tightestConstraintEquation][2] / slackForm[tightestConstraintEquation][1], # b
                        slackForm[tightestConstraintEquation][3] / slackForm[tightestConstraintEquation][1], # c
                        slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][1], # d
                        slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][1], # e 
                        slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][1]] # f
            # print("The rearranged equation is:", newEquation) # this is the rearranged equation

            slackForm2 = [  [slackForm[0][0] + slackForm[0][1] * newEquation[0], 0, slackForm[0][2] + slackForm[0][1] * newEquation[2], slackForm[0][3] + slackForm[0][1] * newEquation[3],  slackForm[0][4] + slackForm[0][1] * newEquation[4],  slackForm[0][5] + slackForm[0][1] * newEquation[5],  slackForm[0][6] + slackForm[0][1] * newEquation[6]], # calories equation
                            [slackForm[1][0] + slackForm[1][1] * newEquation[0], 0, slackForm[1][2] + slackForm[1][1] * newEquation[2], slackForm[1][3] + slackForm[1][1] * newEquation[3],  slackForm[1][4] + slackForm[1][1] * newEquation[4],  slackForm[1][5] + slackForm[1][1] * newEquation[5],  slackForm[1][6] + slackForm[1][1] * newEquation[6]], # fat equation
                            [slackForm[2][0] + slackForm[2][1] * newEquation[0], 0, slackForm[2][2] + slackForm[2][1] * newEquation[2], slackForm[2][3] + slackForm[2][1] * newEquation[3],  slackForm[2][4] + slackForm[2][1] * newEquation[4],  slackForm[2][5] + slackForm[2][1] * newEquation[5],  slackForm[2][6] + slackForm[2][1] * newEquation[6]], # protein equation
                            [slackForm[3][0] + slackForm[3][1] * newEquation[0], 0, slackForm[3][2] + slackForm[3][1] * newEquation[2], slackForm[3][3] + slackForm[3][1] * newEquation[3],  slackForm[3][4] + slackForm[3][1] * newEquation[4],  slackForm[3][5] + slackForm[3][1] * newEquation[5],  slackForm[3][6] + slackForm[3][1] * newEquation[6]]] # cost equation

            slackForm2[tightestConstraintEquation] = newEquation
            slackForm2[tightestConstraintEquation][1] = -1

            # print(slackForm2[0])
            # print(slackForm2[1])
            # print(slackForm2[2])
            # print(slackForm2[3])
            slackForm = slackForm2
            solution[0] = slackForm[tightestConstraintEquation][0]
            # print("Current solution is:", solution)
            # print(slackForm)
        
        # if coefficient of b is positive, maximum can still be achieved; thus, find biggest constraint on b
        if slackForm[0][2] >= 0:

            # finding tightest constraint
            listOfConstraints = []
            listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][2])) # slackForm[1][1]
            listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][2])) # slackForm[2][1]
            listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][2])) # slackForm[3][1]
            tightestConstraint = min(listOfConstraints)
            # print("List of constraints:", listOfConstraints) # fat, protein, cost
            # print("The tightest constraint is:", tightestConstraint) 

            # find the equation where the tighest constraint was found
            tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
            # print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
            tightestConstraintB = tightestConstraintEquation

            slackForm[tightestConstraintEquation][2] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
            # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
            newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][2], # constant
                        slackForm[tightestConstraintEquation][1] / slackForm[tightestConstraintEquation][2], # a
                        1,                                                                                   # b
                        slackForm[tightestConstraintEquation][3] / slackForm[tightestConstraintEquation][2], # c
                        slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][2], # d
                        slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][2], # e 
                        slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][2]] # f
            # print("The rearranged equation is:", newEquation) # this is the rearranged equation

            slackForm2 = [  [slackForm[0][0] + slackForm[0][2] * newEquation[0], slackForm[0][1] + slackForm[0][2] * newEquation[1], 0, slackForm[0][3] + slackForm[0][2] * newEquation[3],  slackForm[0][4] + slackForm[0][2] * newEquation[4],  slackForm[0][5] + slackForm[0][2] * newEquation[5],  slackForm[0][6] + slackForm[0][2] * newEquation[6]], # calories equation
                            [slackForm[1][0] + slackForm[1][2] * newEquation[0], slackForm[1][1] + slackForm[1][2] * newEquation[1], 0, slackForm[1][3] + slackForm[1][2] * newEquation[3],  slackForm[1][4] + slackForm[1][2] * newEquation[4],  slackForm[1][5] + slackForm[1][2] * newEquation[5],  slackForm[1][6] + slackForm[1][2] * newEquation[6]], # fat equation
                            [slackForm[2][0] + slackForm[2][2] * newEquation[0], slackForm[2][1] + slackForm[2][2] * newEquation[1], 0, slackForm[2][3] + slackForm[2][2] * newEquation[3],  slackForm[2][4] + slackForm[2][2] * newEquation[4],  slackForm[2][5] + slackForm[2][2] * newEquation[5],  slackForm[2][6] + slackForm[2][2] * newEquation[6]], # protein equation
                            [slackForm[3][0] + slackForm[3][2] * newEquation[0], slackForm[3][1] + slackForm[3][2] * newEquation[1], 0, slackForm[3][3] + slackForm[3][2] * newEquation[3],  slackForm[3][4] + slackForm[3][2] * newEquation[4],  slackForm[3][5] + slackForm[3][2] * newEquation[5],  slackForm[3][6] + slackForm[3][2] * newEquation[6]]] # cost equation

            slackForm2[tightestConstraintEquation] = newEquation
            slackForm2[tightestConstraintEquation][2] = -1
            

            # print(slackForm2[0])
            # print(slackForm2[1])
            # print(slackForm2[2])
            # print(slackForm2[3])
            
            slackForm = slackForm2
            solution[0] = slackForm[tightestConstraintA][0]
            solution[1] = slackForm[tightestConstraintEquation][0]
            tightestConstraintB = tightestConstraintEquation
            # print(slackForm)
            if tightestConstraintB == tightestConstraintA: solution[0] = 0

        # if coefficient of c is positive, maximum can still be achieved; thus, find biggest constraint on c
        if slackForm[0][3] >= 0:

            # finding tightest constraint
            listOfConstraints = []
            listOfConstraints.append(abs(slackForm[1][0] / slackForm[1][3])) # slackForm[1][1]
            listOfConstraints.append(abs(slackForm[2][0] / slackForm[2][3])) # slackForm[2][1]
            listOfConstraints.append(abs(slackForm[3][0] / slackForm[3][3])) # slackForm[3][1]
            tightestConstraint = min(listOfConstraints)
            # print("List of constraints:", listOfConstraints) # fat, protein, cost
            # print("The tightest constraint is:", tightestConstraint) 

            # find the equation where the tighest constraint was found
            tightestConstraintEquation = listOfConstraints.index(tightestConstraint) + 1
            # print("The equation with the tightest constraint is:", tightestConstraintEquation) # 1 = fat, 2 = protein, 3 = cost 
            tightestConstraintC = tightestConstraintEquation

            slackForm[tightestConstraintEquation][3] *= -1 # when we rearrange, we need to multiply by -1 because we're "moving to the other side"
            # since the tighest constraint here was protein (equation 2), 30/17 = 1.7647, we rearrange e and a in the format a = constant - b - c - e
            newEquation = [slackForm[tightestConstraintEquation][0] / slackForm[tightestConstraintEquation][3], # constant
                        slackForm[tightestConstraintEquation][1] / slackForm[tightestConstraintEquation][3], # a
                        slackForm[tightestConstraintEquation][2] / slackForm[tightestConstraintEquation][3], # b
                        1,                                                                                   # c
                        slackForm[tightestConstraintEquation][4] / slackForm[tightestConstraintEquation][3], # d
                        slackForm[tightestConstraintEquation][5] / slackForm[tightestConstraintEquation][3], # e 
                        slackForm[tightestConstraintEquation][6] / slackForm[tightestConstraintEquation][3]] # f
            # print("The rearranged equation is:", newEquation) # this is the rearranged equation

            slackForm2 = [  [slackForm[0][0] + slackForm[0][3] * newEquation[0], slackForm[0][1] + slackForm[0][3] * newEquation[1], slackForm[0][3] + slackForm[0][3] * newEquation[2], 0,  slackForm[0][4] + slackForm[0][3] * newEquation[4],  slackForm[0][5] + slackForm[0][3] * newEquation[5],  slackForm[0][6] + slackForm[0][3] * newEquation[6]], # calories equation
                            [slackForm[1][0] + slackForm[1][3] * newEquation[0], slackForm[1][1] + slackForm[1][3] * newEquation[1], slackForm[1][3] + slackForm[1][3] * newEquation[2], 0,  slackForm[1][4] + slackForm[1][3] * newEquation[4],  slackForm[1][5] + slackForm[1][3] * newEquation[5],  slackForm[1][6] + slackForm[1][3] * newEquation[6]], # fat equation
                            [slackForm[2][0] + slackForm[2][3] * newEquation[0], slackForm[2][1] + slackForm[2][3] * newEquation[1], slackForm[2][3] + slackForm[2][3] * newEquation[2], 0,  slackForm[2][4] + slackForm[2][3] * newEquation[4],  slackForm[2][5] + slackForm[2][3] * newEquation[5],  slackForm[2][6] + slackForm[2][3] * newEquation[6]], # protein equation
                            [slackForm[3][0] + slackForm[3][3] * newEquation[0], slackForm[3][1] + slackForm[3][3] * newEquation[1], slackForm[3][3] + slackForm[3][3] * newEquation[2], 0,  slackForm[3][4] + slackForm[3][3] * newEquation[4],  slackForm[3][5] + slackForm[3][3] * newEquation[5],  slackForm[3][6] + slackForm[3][3] * newEquation[6]]] # cost equation

            slackForm2[tightestConstraintEquation] = newEquation
            slackForm2[tightestConstraintEquation][3] = -1

            # print(slackForm2[0])
            # print(slackForm2[1])
            # print(slackForm2[2])
            # print(slackForm2[3])
            slackForm = slackForm2
            solution[0] = slackForm[tightestConstraintA][0]
            if tightestConstraintB != None:
                solution[1] = slackForm[tightestConstraintB][0]
            if tightestConstraintC != None:
                solution[2] = slackForm[tightestConstraintEquation][0]
            # print(slackForm)
            if tightestConstraintC == tightestConstraintA: solution[0] = 0
            if tightestConstraintC == tightestConstraintB: solution[1] = 0

        totalCalories = slackForm[0][0]
        McDonalds.solution = solution
        print("FINAL SOLUTION:", solution)
        print("TOTAL CALORIES:", totalCalories)

    def getCachedPhotoImage(mode, image):
        # stores a cached version of the PhotoImage in the PIL/Pillow image
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def displayFoods(mode, canvas):
        resizedImage1 = mode.scaleImage(mode.loadImage(mode.fooditem1[4]), 0.25)
        cachedResizedImage1 = mode.getCachedPhotoImage(resizedImage1)
        canvas.create_image(100, 200, image=cachedResizedImage1)
        canvas.create_text(200, 200 - 10, text=f'{mode.fooditem1name} | Price: ${abs(mode.fooditem1[3])}', anchor='w', font='Calibri 15 bold')
        canvas.create_text(200, 200 + 10, text=f'Calories: {abs(mode.fooditem1[0])} cals | Fat: {abs(mode.fooditem1[1])}g | Protein: {abs(mode.fooditem1[2])}g', anchor='w')
        resizedImage2 = mode.scaleImage(mode.loadImage(mode.fooditem2[4]), 0.25)
        cachedResizedImage2 = mode.getCachedPhotoImage(resizedImage2)
        canvas.create_image(100, 350, image=cachedResizedImage2)
        canvas.create_text(200, 350 - 10, text=f'{mode.fooditem2name} | Price: ${abs(mode.fooditem2[3])}', anchor='w', font='Calibri 15 bold')
        canvas.create_text(200, 350 + 10, text=f'Calories: {abs(mode.fooditem2[0])} cals | Fat: {abs(mode.fooditem2[1])}g | Protein: {abs(mode.fooditem2[2])}g', anchor='w')
        resizedImage3 = mode.scaleImage(mode.loadImage(mode.fooditem3[4]), 0.25)
        cachedResizedImage3 = mode.getCachedPhotoImage(resizedImage3)
        canvas.create_image(100, 500, image=cachedResizedImage3)
        canvas.create_text(200, 500 - 10, text=f'{mode.fooditem3name} | Price: ${abs(mode.fooditem3[3])}', anchor='w', font='Calibri 15 bold')
        canvas.create_text(200, 500 + 10, text=f'Calories: {abs(mode.fooditem3[0])} cals | Fat: {abs(mode.fooditem3[1])}g | Protein: {abs(mode.fooditem3[2])}g', anchor='w')

    def mousePressed(mode, event):
        if (mode.width/2 - 100 <= event.x <= mode.width/2 + 100) and (mode.height - 50 <= event.y <= mode.height):
            # check answer and use mean squared error
            mode.fatDifference = McDonalds.solution[0] - mode.food1Quantity
            mode.proteinDifference = McDonalds.solution[1] - mode.food2Quantity
            mode.costDifference = McDonalds.solution[2] - mode.food3Quantity
            print("Differences:", mode.fatDifference, mode.proteinDifference, mode.costDifference)
            mode.mean_squared_error = (mode.fatDifference**2 + mode.proteinDifference**2 + mode.costDifference**2) / 3
            print("SOLUTION:", McDonalds.solution)
            print("THE MSE IS:", mode.mean_squared_error)
        elif (0 <= event.x <= 100) and (mode.height - 50 <= event.y <= mode.height):
            mode.appStarted()
        elif (550 <= event.x <= 650) and (mode.height - 50 <= event.y <= mode.height):
            mode.showsolution = not mode.showsolution
        elif (500 <= event.x <= 600):
            if (205 <= event.y <= 225): 
                mode.food1Quantity = mode.getUserInput("What quantity? (can be a float, but must be non negative)")
                if mode.food1Quantity != None:
                    mode.quantityReplaced = mode.food1Quantity.replace('.','', 1)
                    while True:
                        if mode.food1Quantity == 0: break
                        elif mode.food1Quantity == None or not mode.quantityReplaced.isdigit() or float(mode.food1Quantity) > 100 or float(mode.food1Quantity) < 0:
                            mode.food1Quantity = mode.getUserInput("How many servings?")
                            if mode.food1Quantity != None:
                                mode.quantityReplaced = mode.food1Quantity.replace('.','', 1)
                        else:
                            mode.food1Quantity = float(mode.food1Quantity)
                            break
                else:
                    mode.food1Quantity = 0
            elif (355 <= event.y <= 375):
                mode.food2Quantity = mode.getUserInput("What quantity? (can be a float, but must be non negative)")
                if mode.food2Quantity != None:
                    mode.quantityReplaced = mode.food2Quantity.replace('.','', 1)
                    while True:
                        if mode.food2Quantity == 0: break
                        elif mode.food2Quantity == None or not mode.quantityReplaced.isdigit() or float(mode.food2Quantity) > 100 or float(mode.food2Quantity) < 0:
                            mode.food2Quantity = mode.getUserInput("How many servings?")
                            if mode.food2Quantity != None:
                                mode.quantityReplaced = mode.food2Quantity.replace('.','', 1)
                        else:
                            mode.food2Quantity = float(mode.food2Quantity)
                            break
                else:
                    mode.food2Quantity = 0
            elif (505 <= event.y <= 525):
                mode.food3Quantity = mode.getUserInput("What quantity? (can be a float, but must be non negative)")
                if mode.food3Quantity != None:
                    mode.quantityReplaced = mode.food3Quantity.replace('.','', 1)
                    while True:
                        if mode.food3Quantity == 0: break
                        elif mode.food3Quantity == None or not mode.quantityReplaced.isdigit() or float(mode.food3Quantity) > 50 or float(mode.food3Quantity) < 0:
                            mode.food3Quantity = mode.getUserInput("How many servings?")
                            if mode.food3Quantity != None:
                                mode.quantityReplaced = mode.food3Quantity.replace('.','', 1)
                        else:
                            mode.food3Quantity = float(mode.food3Quantity)
                            break
                else:
                    mode.food3Quantity = 0
            mode.userCalories = abs(mode.fooditem1[0]) * mode.food1Quantity + abs(mode.fooditem2[0]) * mode.food2Quantity + abs(mode.fooditem3[0]) * mode.food3Quantity
            mode.userFat = abs(mode.fooditem1[1]) * mode.food1Quantity + abs(mode.fooditem2[1]) * mode.food2Quantity + abs(mode.fooditem3[1]) * mode.food3Quantity
            mode.userProtein = abs(mode.fooditem1[2]) * mode.food1Quantity + abs(mode.fooditem2[2]) * mode.food2Quantity + abs(mode.fooditem3[2]) * mode.food3Quantity
            mode.userCost = abs(mode.fooditem1[3]) * mode.food1Quantity + abs(mode.fooditem2[3]) * mode.food2Quantity + abs(mode.fooditem3[3]) * mode.food3Quantity

    def redrawAll(mode, canvas):
        # CITATION: https://www.chick-fil-a.com/about/who-we-are#:~:text=%E2%80%9CTo%20glorify%20God%20by%20being,Chick%2Dfil%2DA.%E2%80%9D
        canvas.create_text(mode.width/2, 25, text="McDonald's Menu", font='Calibri 20 bold') # restaurant name
        canvas.create_text(mode.width/2, 50, text="\"I'm Lovin' It\"", font='Calibri 7 bold') # slogan
        canvas.create_text(mode.width/2, 75, text=f'Objective: maximize total calories, get <={mode.totalFat}g of fat, get <={mode.totalProtein}g of protein, and spend <= ${mode.totalCost}!')
        # canvas.create_text(mode.width/2, 100, text=f'Current Input Results: {mode.userCalories} calories, {mode.userFat}g of fat, {mode.userProtein}g of protein, for ${mode.userCost}')
        canvas.create_text(mode.width/2, 100, text='Current Input Results: %0.4f calories, %0.4fg of fat, %0.4fg of protein, for $%0.2f' % (mode.userCalories, mode.userFat, mode.userProtein, mode.userCost))
        mode.displayFoods(canvas)
        solutiontoggle = 'See Solution'
        if mode.showsolution:
            canvas.create_text(mode.width/2, 625, text='Solution: %0.4f calories, %0.4fg fat, %0.4fg protein, $%0.2f' % (McDonalds.solution[0], McDonalds.solution[1], McDonalds.solution[2], McDonalds.solution[3]))
            solutiontoggle = 'Close Solution'
        canvas.create_rectangle(0, mode.height - 50, 100, mode.height, fill='cyan')
        canvas.create_text(50, mode.height - 25, text='New Puzzle', font='Calibri 10')
        canvas.create_rectangle(550, mode.height - 50, 650, mode.height, fill='cyan')
        canvas.create_text(600, mode.height - 25, text=solutiontoggle, font='Calibri 10')
        canvas.create_rectangle(500, 200 + 5, 600, 200 + 25, fill='cyan')
        canvas.create_text(550, 215, text='Change Quantity', font='Calibri 10')
        canvas.create_text(550, 235, text='Current Quantity: %0.4f' % mode.food1Quantity, font='Calibri 10')
        canvas.create_rectangle(500, 350 + 5, 600, 350 + 25, fill='cyan')
        canvas.create_text(550, 365, text='Change Quantity', font='Calibri 10')
        canvas.create_text(550, 385, text='Current Quantity: %0.4f' % mode.food2Quantity, font='Calibri 10')
        canvas.create_rectangle(500, 500 + 5, 600, 500 + 25, fill='cyan')
        canvas.create_text(550, 515, text='Change Quantity', font='Calibri 10')
        canvas.create_text(550, 535, text='Current Quantity: %0.4f' % mode.food3Quantity, font='Calibri 10')
        canvas.create_rectangle(mode.width/2 - 100, mode.height - 50, mode.width/2 + 100, mode.height, fill='cyan')
        canvas.create_text(mode.width/2, 725, text='Check Answer', font='Calibri 10')
        canvas.create_text(mode.width/2, 650, text='Mean-Squared Error (how far you are from the optimized solution, 0 is the best score!): %0.4f' % mode.mean_squared_error, font='Calibri 11 bold')
        if mode.mean_squared_error <= 10**(-5): canvas.create_text(mode.width/2 + 160, 725, text='You got it!')

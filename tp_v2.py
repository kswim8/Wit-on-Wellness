# Keren Huang Term Project

import module_manager
module_manager.review()
from cmu_112_graphics import *
import random, requests, bs4, json

class SplashScreenMode(Mode):
    def appStarted(mode):
        url = 'https://i.pinimg.com/originals/fe/f7/2f/fef72f73f4f961b4ed6f8e4bb093eb1b.jpg'
        mode.appIcon = mode.loadImage(url)
        mode.appIcon2 = mode.scaleImage(mode.appIcon, 4.5/10)
    
    def mousePressed(mode, event):
        # clicking Sandbox Mode box
        if ((mode.width/4-100) <= event.x <= (mode.width/4+50)) and ((mode.height/2+50) <= event.y <= (mode.height/2+100)):
            mode.app.setActiveMode(mode.app.sandboxMode)
        # clicking Puzzle Mode box
        elif ((mode.width/4-100) <= event.x <= (mode.width/4+50)) and ((3*mode.height/4) <= event.y <= (3*mode.height/4+50)):
            mode.app.setActiveMode(mode.app.puzzleMode)
        # clicking Instructions box
        elif ((3*mode.width/4-50) <= event.x <= (3*mode.width/4+100)) and ((mode.height/2+50) <= event.y <= (mode.height/2+100)):
            mode.app.setActiveMode(mode.app.instructions)
        # clicking Credits box
        elif ((3*mode.width/4-50) <= event.x <= (3*mode.width/4+100)) and ((3*mode.height/4) <= event.y <= (3*mode.height/4+50)):
            mode.app.setActiveMode(mode.app.credits)

    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2, image=ImageTk.PhotoImage(mode.appIcon2))
        canvas.create_text(mode.width/2, mode.height/2-250, text='Wit on Wellness', font='Calibri 26 bold')
        # Sandbox Mode (top left box)
        canvas.create_rectangle(mode.width/4-100, mode.height/2+50, mode.width/4+50, mode.height/2+100, fill='white')
        canvas.create_text(mode.width/4-25, mode.height/2+75, text='Sandbox Mode', font='Calibri 15 bold')
        # Puzzle Mode (bottom left box)
        canvas.create_rectangle(mode.width/4-100, 3*mode.height/4, mode.width/4+50, 3*mode.height/4+50, fill='white')
        canvas.create_text(mode.width/4-25, 3*mode.height/4+25, text='Puzzle Mode', font='Calibri 15 bold')
        # Instructions (top right box)
        canvas.create_rectangle(3*mode.width/4-50, mode.height/2+50, 3*mode.width/4+100, mode.height/2+100, fill='white')
        canvas.create_text(3*mode.width/4+25, mode.height/2+75, text='Instructions', font='Calibri 15 bold')
        # Credits (bottom right box)
        canvas.create_rectangle(3*mode.width/4-50, 3*mode.height/4, 3*mode.width/4+100, 3*mode.height/4+50, fill='white')
        canvas.create_text(3*mode.width/4+25, 3*mode.height/4+25, text='Credits', font='Calibri 15 bold')

class SandboxMode(Mode):
    totalCarbs = 0
    totalProtein = 0
    totalFat = 0
    totalCalories = 0
    userTDEE = None
    userCurrentWeight = None
    userDesiredWeight = None
    userTimeExpected = None
    userGoal = None

    def appStarted(mode):
        mode.results = False
        mode.foodentered = False
        mode.userList = False
        mode.takeUserInputData()
        mode.calculateTDEE()
        mode.userFoodDict = dict()
        mode.userfoodcounter = 0

    def takeUserInputData(mode):
        mode.userGender = mode.getUserInput("What is your biological/current gender (M/F) ?")
        while True:
            if mode.userGender == None or (mode.userGender).upper() != 'M' and (mode.userGender).upper() != 'F':
                mode.userGender = mode.getUserInput("What is your biological/current gender (M/F) ?")
            else:
                break
        mode.userAge = mode.getUserInput("How old are you in years (integer)?")
        while True:
            if mode.userAge == None or not (mode.userAge).isdigit() or int(mode.userAge) > 120 or int(mode.userAge) < 0:
                mode.userAge = mode.getUserInput("How old are you in years (integer)?")
            else:
                mode.userAge = int(mode.userAge)
                break
        mode.userHeight = mode.getUserInput("What is your height in inches (integer)?")
        while True:
            if mode.userHeight == None or not (mode.userHeight).isdigit() or int(mode.userHeight) > 100 or int(mode.userHeight) < 0:
                mode.userHeight = mode.getUserInput("What is your height in inches (integer)?")
            else:
                mode.userHeight = int(mode.userHeight)
                break
        mode.userWeight = mode.getUserInput("What is your weight in pounds (integer)?")
        while True:
            if mode.userWeight == None or not (mode.userWeight).isdigit() or int(mode.userWeight) > 1400 or int(mode.userWeight) < 0:
                mode.userWeight = mode.getUserInput("What is your weight in pounds (integer)?")
            else:
                mode.userWeight = int(mode.userWeight)
                break
        mode.userLevelOfActivity = mode.getUserInput("Rate your level of activity based on these scales:\n 1 = Sedentary (little to no exercise, work a desk job)\n 2 = Lightly Active (light exercise 1-3 days / week)\n 3 = Moderately Active (moderate exercise 3-5 days / week)\n 4 = Very Active (heavy exercise 6-7 days / week)\n 5 = Extremely Active (very heavy exercise, hard labor job, training 2x / day)")
        while True:
            if mode.userLevelOfActivity == None or not (mode.userLevelOfActivity).isdigit() or int(mode.userLevelOfActivity) > 5 or int(mode.userLevelOfActivity) < 1:
                mode.userLevelOfActivity = mode.getUserInput("Rate your level of activity based on these scales:\n 1 = Sedentary (little to no exercise)\n 2 = Lightly Active (light exercise 1-3 days / week)\n 3 = Moderately Active (moderate exercise 3-5 days / week)\n 4 = Very Active (heavy exercise 6-7 days / week)\n 5 = Extremely Active (very heavy exercise, hard labor job, training 2x / day)")
            else:
                mode.userLevelOfActivity = int(mode.userLevelOfActivity)
                break
        mode.userGoal = mode.getUserInput("What is your goal weight (integer)?")
        while True:
            if mode.userGoal == None or not (mode.userGoal).isdigit() or int(mode.userGoal) > 1400 or int(mode.userGoal) < 0:
                mode.userGoal = mode.getUserInput("What is your goal weight (integer)?")
            else:
                mode.userGoal = int(mode.userGoal)
                break
        mode.userTime = mode.getUserInput("In how many days do you want to achieve your target weight (integer)?")
        while True:
            if mode.userTime == None or not (mode.userTime).isdigit() or int(mode.userTime) > 365 or int(mode.userTime) < 1:
                mode.userTime = mode.getUserInput("In how many days do you want to achieve your target weight (integer)?")
            else:
                mode.userTime = int(mode.userTime)
                break
        mode.userGoal2 = mode.getUserInput("Pick the goal that most closely relates to what you're looking for:\n 1 = Lose fat\n 2 = Build muscle\n 3 = Balanced diet")
        while True:
            if mode.userGoal2 == None or not (mode.userGoal2).isdigit() or int(mode.userGoal2) > 3 or int(mode.userGoal2) < 1:
                mode.userGoal2 = mode.getUserInput("Pick the goal that most closely relates to what you're looking for:\n 1 = Lose fat\n 2 = Build muscle\n 3 = Balanced diet")
            else:
                mode.userGoal2 = int(mode.userGoal2)
                break
        SandboxMode.userCurrentWeight = mode.userWeight
        SandboxMode.userDesiredWeight = mode.userGoal
        SandboxMode.userTimeExpected = mode.userTime
        SandboxMode.userGoal = mode.userGoal2
        # print(SandboxMode.userCurrentWeight, SandboxMode.userDesiredWeight, SandboxMode.userTimeExpected)
    
    def calculateTDEE(mode):
        # CITATION: https://steelfitusa.com/2018/10/calculate-tdee/
        # Activity level multipliers to get TDEE
        # Metric Harris-Benedict BMR equation x Activity level multipliers = TDEE
        if mode.userGender == 'M' or 'm':
            mode.userBMR = 66 + 13.7 * (mode.userWeight / 2.2) + 5 * (mode.userHeight * 2.54) - 6.8 * mode.userAge
        elif mode.userGender == 'F' or 'f':
            mode.userBMR = 655 + 9.6 * (mode.userWeight / 2.2) + 1.8 * (mode.userHeight * 2.54) - 4.7 * mode.userAge
        if mode.userLevelOfActivity == 1: mode.userTDEE = 1.2 * mode.userBMR
        elif mode.userLevelOfActivity == 2: mode.userTDEE = 1.375 * mode.userBMR
        elif mode.userLevelOfActivity == 3: mode.userTDEE = 1.55 * mode.userBMR
        elif mode.userLevelOfActivity == 4: mode.userTDEE = 1.725 * mode.userBMR
        elif mode.userLevelOfActivity == 5: mode.userTDEE = 1.9 * mode.userBMR

        SandboxMode.userTDEE = mode.userTDEE

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)
    
    def mousePressed(mode, event):
        if not mode.userList:      
            # search food drink
            if (0 <= event.x <= 200) and (0 <= event.y <= 250):
                userinput = mode.getUserInput("What did you eat or drink today? ")
                if (userinput == None) or len(userinput) == 0:
                    pass
                else:
                    mode.getFoodDict(userinput) 
            # check user list
            elif ((0 <= event.x <= 200) and (250 < event.y <= 500)):
                mode.userList = True
            # results
            elif (0 <= event.x <= 200) and (500 < event.y <= 750):
                mode.results = not mode.results
                mode.app.setActiveMode(mode.app.resultsMode)

            # add to list buttons
            if (mode.foodentered):
                mode.foodselected = False
                if (575 <= event.x <= 650):
                    # CITATION: https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
                    if (45 <= event.y <= 60): # 25
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(25)]
                        mode.foodselected = True
                    elif (120 <= event.y <= 135) and len(mode.foodFullDict) > 1: # 100
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(100)]
                        mode.foodselected = True
                    elif (195 <= event.y <= 210) and len(mode.foodFullDict) > 2: # 175
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(175)]
                        mode.foodselected = True
                    elif (270 <= event.y <= 285) and len(mode.foodFullDict) > 3: # 250
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(250)]
                        mode.foodselected = True
                    elif (345 <= event.y <= 360) and len(mode.foodFullDict) > 4: # 325
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(325)]
                        mode.foodselected = True
                    elif (420 <= event.y <= 435) and len(mode.foodFullDict) > 5: # 400
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(400)]
                        mode.foodselected = True
                    elif (495 <= event.y <= 510) and len(mode.foodFullDict) > 6: # 475
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(475)]
                        mode.foodselected = True
                    elif (570 <= event.y <= 585) and len(mode.foodFullDict) > 7: # 550
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(550)]
                        mode.foodselected = True
                    elif (645 <= event.y <= 660) and len(mode.foodFullDict) > 8: # 625
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(625)]
                        mode.foodselected = True
                    elif (720 <= event.y <= 735) and len(mode.foodFullDict) > 9: # 700
                        newFoodCoord = list(mode.foodFullDictCoords.keys())[list(mode.foodFullDictCoords.values()).index(700)]
                        mode.foodselected = True
                    if mode.foodselected:
                        mode.calculateQuantities(newFoodCoord)

        elif mode.userList:
            if mode.userFoodDict == {} and (((mode.width/2 - 200) <= event.x <= (mode.width/2 + 200)) and ((mode.height/2 + 100) <= event.y <= (mode.height/2 + 200))): 
                mode.userList = False
            else:
                if (mode.width-50 <= event.x <= mode.width) and (0 <= event.y <= 50): 
                    mode.userList = False

    def calculateQuantities(mode, newFoodCoord):
        mode.quantity = mode.getUserInput("How many servings?")
        # CITATION: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
        if mode.quantity != None:
            mode.quantityReplaced = mode.quantity.replace('.','', 1)
            while True:
                if mode.quantity == 0: break
                elif mode.quantity == None or not mode.quantityReplaced.isdigit() or float(mode.quantity) > 100 or float(mode.quantity) < 0:
                    mode.quantity = mode.getUserInput("How many servings?")
                    if mode.quantity != None:
                        mode.quantityReplaced = mode.quantity.replace('.','', 1)
                else:
                    mode.quantity = float(mode.quantity)
                    break
            # finding new quantities for macros based on num of servings
            if mode.quantity != 0:
                newCarbs = mode.quantity * mode.foodFullDict[newFoodCoord][0][0]
                newProteins =  mode.quantity * mode.foodFullDict[newFoodCoord][0][1]
                newFats = mode.quantity * mode.foodFullDict[newFoodCoord][0][2]
                newCalories = mode.quantity * mode.foodFullDict[newFoodCoord][0][3]
                # add to userFoodDict
                mode.userFoodDict[newFoodCoord] = mode.foodFullDict[newFoodCoord] + [mode.quantity] + [(newCarbs, newProteins, newFats, newCalories)] + [85 + 75 * mode.userfoodcounter]
                mode.userfoodcounter += 1
                # increment class attributes
                SandboxMode.totalCarbs += newCarbs
                SandboxMode.totalProtein += newProteins
                SandboxMode.totalFat += newFats
                SandboxMode.totalCalories = SandboxMode.totalCarbs * 4 + SandboxMode.totalProtein * 4 + SandboxMode.totalFat * 9
        # print(SandboxMode.totalCalories)
        # print(mode.userFoodDict)

    # CITATION: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
    def getCachedPhotoImage(mode, image):
        # stores a cached version of the PhotoImage in the PIL/Pillow image
        if ('cachedPhotoImage' not in image.__dict__):
            image.cachedPhotoImage = ImageTk.PhotoImage(image)
        return image.cachedPhotoImage

    def displayFoods(mode, canvas):
        if mode.foodentered:
            for foodname in mode.foodFullDict:
                # cache the image
                resizedImage = mode.scaleImage(mode.loadImage(mode.foodFullDict[foodname][1]), 0.5)
                cachedResizedImage = mode.getCachedPhotoImage(resizedImage)
                # create the cached image
                canvas.create_image(250, mode.foodFullDict[foodname][2], image=cachedResizedImage)
                # display food name and macro counts
                canvas.create_text(300, mode.foodFullDict[foodname][2] - 17.5, text=foodname, font='Calibri 13 bold',anchor='w')
                canvas.create_text(300, mode.foodFullDict[foodname][2], text='Calories: %0.2f' % mode.foodFullDict[foodname][0][3], anchor='w')
                canvas.create_text(300, mode.foodFullDict[foodname][2] + 20, text=f'Carbs (g): {mode.foodFullDict[foodname][0][0]}', anchor='w')
                canvas.create_text(400, mode.foodFullDict[foodname][2] + 20, text=f'Protein (g): {mode.foodFullDict[foodname][0][1]}', anchor='w')
                canvas.create_text(500, mode.foodFullDict[foodname][2] + 20, text=f'Fat (g): {mode.foodFullDict[foodname][0][2]}', anchor='w')
                # separate foods with lines
                canvas.create_line(200, mode.foodFullDict[foodname][2] + 37.5, mode.width, mode.foodFullDict[foodname][2] + 37.5)
                # add-to-list button
                canvas.create_rectangle(575, mode.foodFullDict[foodname][2] + 20, 650, mode.foodFullDict[foodname][2] + 35, fill='cyan')
                canvas.create_text(612.5, mode.foodFullDict[foodname][2] + 27.5, text='Add to List')
    
    def displayUserFoods(mode, canvas):
        for foodname in mode.userFoodDict:
            resizedImage = mode.scaleImage(mode.loadImage(mode.userFoodDict[foodname][1]), 0.5)
            cachedResizedImage = mode.getCachedPhotoImage(resizedImage)
            # create the cached image
            canvas.create_image(50, mode.userFoodDict[foodname][5], image=cachedResizedImage)
            # display food name and macro counts
            canvas.create_text(100, mode.userFoodDict[foodname][5] - 17.5, text=foodname, font='Calibri 13 bold',anchor='w')
            canvas.create_text(100, mode.userFoodDict[foodname][5], text='Calories: %0.2f' % mode.userFoodDict[foodname][4][3], anchor='w')
            canvas.create_text(100, mode.userFoodDict[foodname][5] + 20, text=f'Quantity (servings): {mode.userFoodDict[foodname][3]}', anchor='w')
            canvas.create_text(230, mode.userFoodDict[foodname][5] + 20, text='Total Carbs (g): %0.2f' % mode.userFoodDict[foodname][4][0], anchor='w')
            canvas.create_text(360, mode.userFoodDict[foodname][5] + 20, text='Total Protein (g): %0.2f' % mode.userFoodDict[foodname][4][1], anchor='w')
            canvas.create_text(490, mode.userFoodDict[foodname][5] + 20, text='Total Fat (g): %0.2f' % mode.userFoodDict[foodname][4][2], anchor='w')
            # separate foods with lines
            canvas.create_line(0, mode.userFoodDict[foodname][5] + 37.5, mode.width, mode.userFoodDict[foodname][5] + 37.5)

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
                # mode.foodFullDict[foodname] = (proteinContent, fatContent, carbContent)
                calories = carbContent * 4 + proteinContent * 4 + fatContent * 9
                mode.foodFullDict[foodname] = (carbContent, proteinContent, fatContent, calories)

        except IndexError:
            # if there are no search results, print this and repeat
            if len(foodset) == 0:
                mode.showMessage(f"Could not find a food or drink labeled {userinput}, please try again.")
            # otherwise, there's probably some single or <10 elements

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
        if not mode.userList:
            canvas.create_line(200, 0, 200, mode.height)     
            canvas.create_rectangle(0, 0, 200, 250, fill='red')
            canvas.create_text(100, 125, text='Search Food / Drink', font='Calibri 15 bold')
            canvas.create_rectangle(0, 250, 200, 500, fill='yellow')
            canvas.create_text(100, 375, text='Check Current User List', font='Calibri 15 bold')
            canvas.create_rectangle(0, 500, 200, 750, fill='green')
            canvas.create_text(100, 625, text='See Results', font='Calibri 15 bold')    
            mode.displayFoods(canvas)
        elif mode.userList:
            if mode.userFoodDict == {}: 
                canvas.create_text(mode.width/2, mode.height/2, text='You have no foods or drinks in your list.', font='Calibri 15 bold')
                canvas.create_rectangle(mode.width/2 - 200, mode.height/2 + 100, mode.width/2 + 200, mode.height/2 + 200, fill='cyan')
                canvas.create_text(mode.width/2, mode.height/2 + 150, text='Go Back to Search & Add Food / Drinks', font='Calibri 12 bold')
            else:
                canvas.create_text(5, 25, text='User List of Foods / Drinks', font='Calibri 15 bold', anchor='w')
                canvas.create_line(0, 50, mode.width, 50)
                # canvas.create_text(250, 25, text='Total Carbs (g): %0.2f' % mode.totalCarbs, anchor='w') # total carbs
                # canvas.create_text(375, 25, text='Total Protein (g): %0.2f' % mode.totalProtein, anchor='w') # total proteins
                # canvas.create_text(500, 25, text='Total Fat (g): %0.2f' % mode.totalFat, anchor='w') # total fats
                canvas.create_text(235, 25 - 10, text='Total Calories: %0.2f' % SandboxMode.totalCalories, anchor='w')
                canvas.create_text(235, 25 + 10, text='Total Carbs (g): %0.2f' % SandboxMode.totalCarbs, anchor='w') # total carbs
                canvas.create_text(360, 25 + 10, text='Total Protein (g): %0.2f' % SandboxMode.totalProtein, anchor='w') # total proteins
                canvas.create_text(485, 25 + 10, text='Total Fat (g): %0.2f' % SandboxMode.totalFat, anchor='w') # total fats
                canvas.create_rectangle(mode.width - 50, 0, mode.width, 50, fill='cyan') # back button
                canvas.create_text(mode.width - 25, 25, text='Back', font='Calibri 10 bold')
                mode.displayUserFoods(canvas)

class Results(SandboxMode):
    def appStarted(mode):
        mode.carbsText = False
        mode.proteinText = False
        mode.fatText = False

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.sandboxMode)

    def mousePressed(mode, event):
        # back to home screen button
        if SandboxMode.totalCalories == 0:
            if (mode.width/2 - 100 <= event.x <= mode.width/2 + 100) and (mode.height/2 + 100 <= event.y <= mode.height/2 + 300):
                mode.app.setActiveMode(mode.app.sandboxMode)
        pass

    def mouseMoved(mode, event):
        # show the exact percentage over the bar and a message about the macro itself in relation to user goal
        if SandboxMode.totalCalories != 0:
            if (65 <= event.x <= 65 + mode.carbsBar[0] * 250) and (150 - 5 <= event.y <= 150 + 5):
                mode.carbsText = True
                mode.proteinText = False
                mode.fatText = False
                # canvas.create_text(65 + mode.carbsBar[0] * 250, 150, text=mode.carbsProportion, anchor='w')
            elif (65 <= event.x <= 65 + mode.proteinBar[0] * 250) and (225 - 5 <= event.y <= 225 + 5):
                mode.carbsText = False
                mode.proteinText = True
                mode.fatText = False
                # canvas.create_text(65 + mode.proteinBar[0] * 250, 150, text=mode.proteinProportion, anchor='w')
            elif (65 <= event.x <= 65 + mode.fatBar[0] * 250) and (300 - 5 <= event.y <= 300 + 5):
                mode.carbsText = False
                mode.proteinText = False
                mode.fatText = True
                # canvas.create_text(65 + mode.fatBar[0] * 250, 150, text=mode.fatProportion, anchor='w')
        pass

    def findProportions(mode):
        # CITATION: https://kidshealth.org/en/teens/fat-calories.html#:~:text=A%20gram%20of%20carbohydrate%20contains,amount%20of%20the%20other%20two.
        mode.carbsProportion = 4 * SandboxMode.totalCarbs / SandboxMode.totalCalories
        mode.proteinProportion = 4 * SandboxMode.totalProtein / SandboxMode.totalCalories
        mode.fatProportion = 9 * SandboxMode.totalFat / SandboxMode.totalCalories
    
    def checkProportions(mode):
        # check for user's goal (lose fat, build muscle, etc.)
        # return a tuple of bar colors and bar heights

        mode.findProportions()
        # fat loss
        # CITATION: https://www.womenshealthmag.com/uk/food/healthy-eating/a705352/best-macros-for-fat-loss/
        if SandboxMode.userGoal == 1:
            # 50, 35, 15, give or take 5
            if (0.45 <= mode.carbsProportion <= 0.55): mode.carbBarColor = 'green'
            elif (0.40 <= mode.carbsProportion <= 0.60): mode.carbBarColor = 'yellow'
            elif mode.carbsProportion < 0.40 or mode.carbsProportion > 0.60: mode.carbBarColor = 'red'

            if (0.30 <= mode.proteinProportion <= 0.40): mode.proteinBarColor = 'green'
            elif (0.25 <= mode.proteinProportion <= 0.45): mode.proteinBarColor = 'yellow'
            elif mode.proteinProportion < 0.25 or mode.proteinProportion > 0.45: mode.proteinBarColor = 'red'

            if (0.10 <= mode.fatProportion <= 0.20): mode.fatBarColor = 'green'
            elif (0.05 <= mode.fatProportion <= 0.25): mode.fatBarColor = 'yellow'
            elif mode.fatProportion < 0.05 or mode.fatProportion > 0.25: mode.fatBarColor = 'red'

            mode.carbsBar = [mode.carbsProportion, mode.carbBarColor]
            mode.proteinBar = [mode.proteinProportion, mode.proteinBarColor]
            mode.fatBar = [mode.fatProportion, mode.fatBarColor]

        # muscle gain
        # CITATION: https://lifesum.com/health-education/how-to-count-macros-for-building-muscle-and-losing-fat/#:~:text=A%20typical%20macro%20breakdown%20for,two%20different%20types%20of%20mass.
        elif SandboxMode.userGoal == 2:
            # 30, 40, 30, give or take 5
            if (0.25 <= mode.carbsProportion <= 0.35): mode.carbBarColor = 'green'
            elif (0.20 <= mode.carbsProportion <= 0.40): mode.carbBarColor = 'yellow'
            elif mode.carbsProportion < 0.20 or mode.carbsProportion > 0.40: mode.carbBarColor = 'red'

            if (0.35 <= mode.proteinProportion <= 0.45): mode.proteinBarColor = 'green'
            elif (0.30 <= mode.proteinProportion <= 0.55): mode.proteinBarColor = 'yellow'
            elif mode.proteinProportion < 0.30 or mode.proteinProportion > 0.50: mode.proteinBarColor = 'red'

            if (0.10 <= mode.fatProportion <= 0.20): mode.fatBarColor = 'green'
            elif (0.05 <= mode.fatProportion <= 0.25): mode.fatBarColor = 'yellow'
            elif mode.fatProportion < 0.05 or mode.fatProportion > 0.25: mode.fatBarColor = 'red'

            mode.carbsBar = [mode.carbsProportion, mode.carbBarColor]
            mode.proteinBar = [mode.proteinProportion, mode.proteinBarColor]
            mode.fatBar = [mode.fatProportion, mode.fatBarColor]

        # balanced diet
        elif SandboxMode.userGoal == 3:
            # 50, 25, 25, give or take 5
            if (0.45 <= mode.carbsProportion <= 0.55): mode.carbBarColor = 'green'
            elif (0.40 <= mode.carbsProportion <= 0.60): mode.carbBarColor = 'yellow'
            elif mode.carbsProportion < 0.40 or mode.carbsProportion > 0.60: mode.carbBarColor = 'red'

            if (0.20 <= mode.proteinProportion <= 0.30): mode.proteinBarColor = 'green'
            elif (0.15 <= mode.proteinProportion <= 0.35): mode.proteinBarColor = 'yellow'
            elif mode.proteinProportion < 0.15 or mode.proteinProportion > 0.35: mode.proteinBarColor = 'red'

            if (0.20 <= mode.fatProportion <= 0.30): mode.fatBarColor = 'green'
            elif (0.15 <= mode.fatProportion <= 0.35): mode.fatBarColor = 'yellow'
            elif mode.fatProportion < 0.15 or mode.fatProportion > 0.35: mode.fatBarColor = 'red'

            mode.carbsBar = [mode.carbsProportion, mode.carbBarColor]
            mode.proteinBar = [mode.proteinProportion, mode.proteinBarColor]
            mode.fatBar = [mode.fatProportion, mode.fatBarColor]

    def drawBarGraph(mode, canvas):
        canvas.create_text(mode.width/4, 55, text='Macronutrient Proportions', font='Calibri 15 bold') # graph title
        canvas.create_text(190, 385, text='Percentages of Whole Meal', font='Calibri 10 bold') # x axis label - proportion of whole meal
        # canvas.create_text() # y axis label - macronutrients
        
        # x axis, proportions
        canvas.create_text(65, 367, text='0.0', font='Calibri 10 bold') # 0
        canvas.create_text(115, 367, text='0.2', font='Calibri 10 bold') # 0.2
        canvas.create_text(165, 367, text='0.4', font='Calibri 10 bold') # 0.4
        canvas.create_text(215, 367, text='0.6', font='Calibri 10 bold') # 0.6
        canvas.create_text(265, 367, text='0.8', font='Calibri 10 bold') # 0.8
        canvas.create_text(315, 367, text='1.0', font='Calibri 10 bold') # 1.0
        canvas.create_line(65, 100, 315, 100) # x axis (top)
        canvas.create_line(65, 350, 315, 350) # x axis (bottom

        # y axis, macros (horizontal bars)
        canvas.create_text(55, 150, text='CARBS', anchor='e', font='Calibri 10 bold') # carbs
        canvas.create_text(55, 225, text='PROTEIN', anchor='e', font='Calibri 10 bold') # protein
        canvas.create_text(55, 300, text='FAT', anchor='e', font='Calibri 10 bold') # fat
        canvas.create_line(65, 100, 65, 350) # y axis (left)
        canvas.create_line(315, 100, 315, 350) # y axis (right)
        
        mode.checkProportions() # get bar heights and colors
        canvas.create_rectangle(65, 150 - 5, 65 + mode.carbsBar[0] * 250,     150 + 5, fill=mode.carbsBar[1])     # carbs
        canvas.create_rectangle(65, 225 - 5, 65 + mode.proteinBar[0] * 250,   225 + 5, fill=mode.proteinBar[1])   # protein
        canvas.create_rectangle(65, 300 - 5, 65 + mode.fatBar[0] * 250,       300 + 5, fill=mode.fatBar[1])       # fat 

        # text advice
        if mode.carbsText:
            canvas.create_text(70 + mode.carbsBar[0] * 250, 150, text='%0.4f' % mode.carbsProportion, anchor='w')
            if mode.carbsBar[1] == 'green':
                canvas.create_text(55, 450, text='You are taking the right percentage\nof carbs to meet your goal!', font='Calibri 12', anchor='w')
            
            elif mode.carbsBar[1] == 'yellow':
                canvas.create_text(55, 450, text='You are taking an alright percentage\nof carbs to meet your goal, but try\nto get closer to the range shown below!', font='Calibri 12', anchor='w')
                if SandboxMode.userGoal == 1:
                    canvas.create_text(mode.width/4, 500, text='0.45 to 0.55 for losing fat', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 2:
                    canvas.create_text(mode.width/4, 500, text='0.25 to 0.35 for building muscle', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 3:
                    canvas.create_text(mode.width/4, 500, text='0.45 to 0.55 for balanced diet', font='Calibri 12 bold')

            elif mode.carbsBar[1] == 'red':
                canvas.create_text(55, 450, text='You are not taking the right percentage\nof carbs to meet your goal, try to\nget around the range shown below!', font='Calibri 12', anchor='w')
                if SandboxMode.userGoal == 1:
                    canvas.create_text(mode.width/4, 500, text='0.45 to 0.55 for losing fat', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 2:
                    canvas.create_text(mode.width/4, 500, text='0.25 to 0.35 for building muscle', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 3:
                    canvas.create_text(mode.width/4, 500, text='0.45 to 0.55 for balanced diet', font='Calibri 12 bold')
            
            # CITATION: https://www.nhs.uk/live-well/healthy-weight/why-we-need-to-eat-carbs/#:~:text=Carbohydrates%20are%20the%20body's%20main,important%20for%20long%2Dterm%20health.
            canvas.create_text(55, 550, text='Carbs are important because they are\nthe main source of energy for the body.', font='Calibri 12', anchor='w')
            # CITATION: https://www.myfooddata.com/articles/foods-highest-in-carbohydrates.php
            canvas.create_text(55, 650, text='High-carb foods include grains (bread,\nrice, cereal), fruit, and more! ', font='Calibri 12', anchor='w')

        elif mode.proteinText:
            canvas.create_text(70 + mode.proteinBar[0] * 250, 225, text='%0.4f' % mode.proteinProportion, anchor='w')
            if mode.proteinBar[1] == 'green':
                canvas.create_text(55, 450, text='You are taking the right percentage\nof protein to meet your goal!', font='Calibri 12', anchor='w')
            
            elif mode.proteinBar[1] == 'yellow':
                canvas.create_text(55, 450, text='You are taking an alright percentage\nof protein to meet your goal, but try\nto get closer to the range shown below!', font='Calibri 12', anchor='w')
                if SandboxMode.userGoal == 1:
                    canvas.create_text(mode.width/4, 500, text='0.30 to 0.40 for losing fat', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 2:
                    canvas.create_text(mode.width/4, 500, text='0.35 to 0.45 for building muscle', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 3:
                    canvas.create_text(mode.width/4, 500, text='0.20 to 0.30 for balanced diet', font='Calibri 12 bold')

            elif mode.proteinBar[1] == 'red':
                canvas.create_text(55, 450, text='You are not taking the right percentage\nof protein to meet your goal, try to\nget around the range shown below!', font='Calibri 12', anchor='w')
                if SandboxMode.userGoal == 1:
                    canvas.create_text(mode.width/4, 500, text='0.30 to 0.40 for losing fat', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 2:
                    canvas.create_text(mode.width/4, 500, text='0.35 to 0.45 for building muscle', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 3:
                    canvas.create_text(mode.width/4, 500, text='0.20 to 0.30 for balanced diet', font='Calibri 12 bold')

            # CITATION: https://www.piedmont.org/living-better/why-is-protein-important-in-your-diet
            canvas.create_text(55, 550, text='Protein is important because it builds,\nrepairs, and maintains cells, muscles,\nand tissue.', font='Calibri 12', anchor='w')
            # CITATION: https://www.healthline.com/nutrition/20-delicious-high-protein-foods
            canvas.create_text(55, 650, text='High-protein foods include eggs,\nseafood, nuts, poultry, and more!', font='Calibri 12', anchor='w')

        elif mode.fatText: 
            canvas.create_text(70 + mode.fatBar[0] * 250, 300, text='%0.4f' % mode.fatProportion, anchor='w')
            if mode.fatBar[1] == 'green':
                canvas.create_text(55, 450, text='You are taking the right percentage\nof fat to meet your goal!', font='Calibri 12', anchor='w')
            
            elif mode.fatBar[1] == 'yellow':
                canvas.create_text(55, 450, text='You are taking an alright percentage\nof fat to meet your goal, but try\nto get closer to the range shown below!', font='Calibri 12', anchor='w')
                if SandboxMode.userGoal == 1:
                    canvas.create_text(mode.width/4, 500, text='0.10 to 0.20 for losing fat', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 2:
                    canvas.create_text(mode.width/4, 500, text='0.25 to 0.35 for building muscle', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 3:
                    canvas.create_text(mode.width/4, 500, text='0.15 to 0.25 for balanced diet', font='Calibri 12 bold')

            elif mode.fatBar[1] == 'red':
                canvas.create_text(55, 450, text='You are not taking the right percentage\nof fat to meet your goal, try to\nget around the range shown below!', font='Calibri 12', anchor='w')
                if SandboxMode.userGoal == 1:
                    canvas.create_text(mode.width/4, 500, text='0.10 to 0.20 for losing fat', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 2:
                    canvas.create_text(mode.width/4, 500, text='0.25 to 0.35 for building muscle', font='Calibri 12 bold')
                elif SandboxMode.userGoal == 3:
                    canvas.create_text(mode.width/4, 500, text='0.15 to 0.25 for balanced diet', font='Calibri 12 bold')

            # CITATION: https://www.nhs.uk/live-well/eat-well/different-fats-nutrition/#:~:text=A%20small%20amount%20of%20fat,with%20the%20help%20of%20fats.
            canvas.create_text(55, 550, text='Fat is important for the body because\nwe need to absorb vitamin A/D/E,\nwhich fat does a good job of.', font='Calibri 12', anchor='w')
            # CITATION: https://www.healthline.com/nutrition/10-super-healthy-high-fat-foods
            canvas.create_text(55, 650, text='Healthy, high-fat foods include\navocados, cheese, nuts,\neggs, and more!', font='Calibri 12', anchor='w')
        
        else:
            canvas.create_text(55, 450, text='Hover over any bar above to get\nmore information and feedback\nabout your food plan!', font='Calibri 12', anchor='w')

    def drawLinePlot(mode, canvas):
        canvas.create_text(3*mode.width/4, 55, text='Time Plan', font='Calibri 15 bold') # graph title
        canvas.create_text(515, 385, text='Number of Days', font='Calibri 10 bold') # number of days

        if SandboxMode.userCurrentWeight == SandboxMode.userDesiredWeight:
            canvas.create_text(380, 225, text=SandboxMode.userCurrentWeight, font='Calibri 10 bold', anchor='e')
            mode.daysMax = SandboxMode.userTimeExpected
            canvas.create_text(640, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
            canvas.create_line(390, 225, 640, 225)
            # print("To maintain weight, try to eat about", SandboxMode.userTDEE, "calories per day and maintain consistent exercise levels.")
            canvas.create_text(380, 450, text='To maintain weight, try to eat\nabout %0.1f calories per day and\nmaintain consistent exercise levels.' % SandboxMode.userTDEE, anchor='w', font='Calibri 12')
        else:
            if SandboxMode.userCurrentWeight > SandboxMode.userDesiredWeight:
                mode.caloriesToLosePerDay = 3500 * (SandboxMode.userCurrentWeight - SandboxMode.userDesiredWeight) / SandboxMode.userTimeExpected
                # print(mode.caloriesToLosePerDay)
                if mode.caloriesToLosePerDay > 1000:
                    mode.daysMin = 3500 * (SandboxMode.userCurrentWeight - SandboxMode.userDesiredWeight) / 1000
                    mode.daysMax = 3500 * (SandboxMode.userCurrentWeight - SandboxMode.userDesiredWeight) / 500
                    canvas.create_text(515, 367, text='%0.1f' % mode.daysMin, font='Calibri 10 bold') # min days
                    canvas.create_text(640, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
                    canvas.create_text(380, 183, text=SandboxMode.userCurrentWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_text(380, 266, text=SandboxMode.userDesiredWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_line(390, 183, 640, 266)
                    canvas.create_text(380, 450, text='Realistically, you should try to\nlose this weight in %0.1f to\n%0.1f days.' % (mode.daysMin, mode.daysMax), anchor='w', font='Calibri 12')
                    canvas.create_text(380, 525, text='This means still eating at least\n%0.1f and at most %0.1f calories\nper day while exercising consistently\nfor healthy weight loss!' % (SandboxMode.userTDEE - 1000, SandboxMode.userTDEE - 500), anchor='w', font='Calibri 12')
                    # print("Realistically, you should try to lose this weight in", mode.daysMin, "to", mode.daysMax, "days.")
                    # print("This means still eating at least", (SandboxMode.userTDEE - 1000), "and at most", (SandboxMode.userTDEE - 500),"calories per day while exercising consistently for healthy weight loss!")
                else:
                    mode.daysMax = SandboxMode.userTimeExpected
                    canvas.create_text(380, 183, text=SandboxMode.userCurrentWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_text(380, 266, text=SandboxMode.userDesiredWeight, anchor='e', font='Calibri 10 bold')
                    canvas.create_text(640, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
                    canvas.create_line(390, 183, 640, 266)
                    canvas.create_text(380, 450, text='You need to eat about\n%0.1f less calories per day\nto reach your goal.' % (mode.caloriesToLosePerDay), anchor='w', font='Calibri 12')
                    canvas.create_text(380, 525, text='This means eating about\n%0.1f calories per day while\nexercising consistently!' % (SandboxMode.userTDEE - mode.caloriesToLosePerDay), anchor='w', font='Calibri 12')
                    # print("You need to eat about", mode.caloriesToLosePerDay, "less calories per day to reach your goal.")
                    # print("This means eating about", (SandboxMode.userTDEE - mode.caloriesToLosePerDay), "calories per day while exercising consistently!")
            elif SandboxMode.userCurrentWeight < SandboxMode.userDesiredWeight:
                mode.caloriesToGainPerDay = 3500 * (SandboxMode.userCurrentWeight - SandboxMode.userDesiredWeight) / SandboxMode.userTimeExpected
                # print(mode.caloriesToGainPerDay)
                if mode.caloriesToGainPerDay > 1000:
                    mode.daysMin = 3500 * (SandboxMode.userDesiredWeight - SandboxMode.userCurrentWeight) / 1000
                    mode.daysMax = 3500 * (SandboxMode.userDesiredWeight - SandboxMode.userCurrentWeight) / 500
                    canvas.create_text(380, 183, text=SandboxMode.userDesiredWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_text(380, 266, text=SandboxMode.userCurrentWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_text(515, 367, text='%0.1f' % mode.daysMin, font='Calibri 10 bold') # min days
                    canvas.create_text(640, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
                    canvas.create_line(390, 266, 640, 183)
                    canvas.create_text(380, 450, text='Realistically, you should try to\ngain this weight in %0.1f to\n%0.1f days.' % (mode.daysMin, mode.daysMax), anchor='w')
                    canvas.create_text(380, 525, text='This means still eating at least\n%0.1f and at most %0.1f calories\nper day while exercising consistently\nfor healthy weight gain!' % (SandboxMode.userTDEE + 500, SandboxMode.userTDEE + 1000), anchor='w', font='Calibri 12')
                    # print("Realistically, you should try to gain this weight in", mode.daysMin, "to", mode.daysMax, "days.")
                    # print("This means eating at most", (SandboxMode.userTDEE - 1000), "calories per day while exercising consistently for healthy weight gain!")
                else:
                    mode.daysMax = SandboxMode.userTimeExpected
                    canvas.create_text(380, 183, text=SandboxMode.userCurrentWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_text(380, 266, text=SandboxMode.userDesiredWeight, anchor='e', font='Calibri 10 bold')
                    canvas.create_text(640, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
                    canvas.create_line(390, 266, 640, 183)
                    canvas.create_text(380, 450, text='You need to eat about\n%0.1f more calories per day\nto reach your goal.' % (mode.caloriesToGainPerDay), anchor='w', font='Calibri 12')
                    canvas.create_text(380, 525, text='This means eating about\n%0.1f calories per day while\nexercising consistently!' % (SandboxMode.userTDEE + mode.caloriesToGainPerDay), anchor='w', font='Calibri 12')
                    # print("You need to eat about", mode.caloriesToLosePerDay, "more calories per day to reach your goal.")
                    # print("This means eating about", (SandboxMode.userTDEE - mode.caloriesToLosePerDay), "calories per day while exercising consistently!")

        # x axis, proportions
        canvas.create_text(390, 367, text='0', font='Calibri 10 bold') # 0

        canvas.create_line(390, 100, 640, 100) # x axis (top)
        canvas.create_line(390, 350, 640, 350) # x axis (bottom)

         # y axis, macros (horizontal bars)
        canvas.create_line(390, 100, 390, 350) # y axis (left)
        canvas.create_line(640, 100, 640, 350) # y axis (right)

        canvas.create_text(380, 600, text='TDEE: %0.2f calories' % SandboxMode.userTDEE, font='Calibri 12 bold', anchor='w') # tdee
        canvas.create_text(380, 675, text='TDEE (Total daily energy expenditure):\nhow many calories you are expected to burn.\nUsing this value, we can find how many more\nor less calories should be consumed to\ngain or lose weight. ', anchor='w')
        
        # canvas.create_text(380, 615, text='Expected Carbs: %0.2f' % (SandboxMode.userTDEE * 4), font='Calibri 10', anchor='w') # expected carbs
        # canvas.create_text(380, 630, text='Expected Protein: %0.2f' % (SandboxMode.totalProtein * 4), font='Calibri 10', anchor='w') # expected protein
        # canvas.create_text(380, 645, text='Expected Fat: %0.2f' % (SandboxMode.totalFat * 9), font='Calibri 10', anchor='w') # expected fat

        # canvas.create_text(380, 680, text='Calories: %0.2f' % SandboxMode.totalCalories, font='Calibri 10', anchor='w') # current cals
        # canvas.create_text(380, 695, text='Current Carbs: %0.2f' % (SandboxMode.totalCarbs * 4), font='Calibri 10', anchor='w') # current carbs
        # canvas.create_text(380, 710, text='Current Protein: %0.2f' % (SandboxMode.totalProtein * 4), font='Calibri 10', anchor='w') # current protein
        # canvas.create_text(380, 725, text='Current Fat: %0.2f' % (SandboxMode.totalFat * 9), font='Calibri 10', anchor='w') # current fat
    
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, 40, fill='cyan')
        canvas.create_text(mode.width/2, 20, text='Results', font='Calibri 15 bold')
        if SandboxMode.totalCalories == 0:
            canvas.create_text(mode.width/2, mode.height/2, text='No results to show.', font='Calibri 15 bold')
            canvas.create_rectangle(mode.width/2 - 100, mode.height/2 + 150, mode.width/2 + 100, mode.height/2 + 250, fill='cyan')
            canvas.create_text(mode.width/2, mode.height/2 + 200, text='Go Back to Sandbox', font='Calibri 15 bold')
        else:
            canvas.create_line(mode.width/2, 40, mode.width/2, mode.height)
            mode.findProportions()
            mode.drawBarGraph(canvas)
            mode.drawLinePlot(canvas)

class PuzzleMode(Mode):
    def appStarted(mode):
        mode.puzzle1 = False
        mode.puzzle2 = False

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

    def mousePressed(mode, event):
        if (0 <= event.x <= 200) and (0 <= event.y <= 375): 
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

# Puzzle 1: Highest Calorie Food
class PuzzleMode1(PuzzleMode):
    pass

# Puzzle 2: Food Choice Optimization (LINEAR PROGRAMMING)
class PuzzleMode2(PuzzleMode):
    pass

class Instructions(Mode):
    def appStarted(mode):
        url = 'https://i.pinimg.com/originals/fe/f7/2f/fef72f73f4f961b4ed6f8e4bb093eb1b.jpg'
        mode.appIcon = mode.loadImage(url)
        mode.appIcon2 = mode.scaleImage(mode.appIcon, 4.5/10)
        filename1 = 'sandboxmodepic.png'
        mode.sandboxImage = mode.loadImage(filename1)
        mode.sandboxImage2 = mode.scaleImage(mode.sandboxImage, 0.45)
        filename2 = 'puzzlemodepic.png'
        mode.puzzleImage = mode.loadImage(filename2)
        mode.puzzleImage2 = mode.scaleImage(mode.puzzleImage, 0.45)

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

    def mousePressed(mode, event):
        if ((mode.width/4 - 75 <= event.x <= mode.width/4 + 75) and (35 <= event.y <= 65)) or ((mode.width/4 - 100 <= event.x <= mode.width/4 + 100) and (670 <= event.y <= 700)): mode.app.setActiveMode(mode.app.sandboxMode)
        elif ((3*mode.width/4 - 75 <= event.x <= 3*mode.width/4 + 75) and (35 <= event.y <= 65)) or ((3*mode.width/4 - 100 <= event.x <= 3*mode.width/4 + 100) and (670 <= event.y <= 700)): mode.app.setActiveMode(mode.app.puzzleMode)
    
    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2, image=ImageTk.PhotoImage(mode.appIcon2))
        canvas.create_rectangle(mode.width/4 - 75, 35, mode.width/4 + 75, 65, fill='white')
        canvas.create_rectangle(3*mode.width/4 - 75, 35, 3*mode.width/4 + 75, 65, fill='white')
        canvas.create_rectangle(0, 3*mode.height/4 - 100, mode.width, 3*mode.height/4 + 100, fill='white')
        canvas.create_line(mode.width/2, 3*mode.height/4 - 100, mode.width/2, 3*mode.height/4 + 100)

        canvas.create_rectangle(mode.width/4 - 100, 670, mode.width/4 + 100, 700, fill='white')
        canvas.create_rectangle(3*mode.width/4 - 100, 670, 3*mode.width/4 + 100, 700, fill='white')
        canvas.create_text(mode.width/4, 685, text='Play Sandbox Mode', font='Calibri 15 bold')
        canvas.create_text(3*mode.width/4, 685, text='Play Puzzle Mode', font='Calibri 15 bold')

        canvas.create_text(mode.width/2, 20, text='Instructions', font='Calibri 18 bold')
        canvas.create_text(mode.width/4, 50, text='Sandbox Mode', font='Calibri 15 bold')
        canvas.create_image(mode.width/4, mode.height/2 - 100, image=ImageTk.PhotoImage(mode.sandboxImage2))
        canvas.create_text(3*mode.width/4, 50, text='Puzzle Mode', font='Calibri 15 bold')
        canvas.create_image(3*mode.width/4, mode.height/2 - 100, image=ImageTk.PhotoImage(mode.puzzleImage2))
        canvas.create_text(mode.width/4, 3*mode.height/4,   text='In Sandbox Mode, you can experiment\nwith different foods and diets and\nmake your own food plan! You can\nlearn about what kind of goals you can set,\nas well as receive feedback and\nresults about your goals.', font='Calibri 12')
        canvas.create_text(3*mode.width/4, 3*mode.height/4, text='In Puzzle Mode, you can try solving\nthe different puzzles given a certain\nscenario! You can learn about\noptimizing ingredients or picking the best\nfoods to eat when you are trying\nto meet a goal.', font='Calibri 12')
        pass

class Credits(Mode):
    def appStarted(mode):
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

    def redrawAll(mode, canvas):
        # canvas.create_text(mode.width/2, mode.height/2, text='Keren Huang\nMentor: Alex Xie')
        pass

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.sandboxMode = SandboxMode()
        app.resultsMode = Results()
        app.puzzleMode = PuzzleMode()
        app.puzzleMode1 = PuzzleMode1()
        app.puzzleMode2 = PuzzleMode2()
        app.instructions = Instructions()
        app.credits = Credits()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=650, height=750)
# Keren Huang Term Project

import module_manager
module_manager.review()
from cmu_112_graphics import *
import random, requests, bs4, json, numpy
from matplotlib import pyplot as plt
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    def appStarted(mode):
        mode.results = False
        mode.foodentered = False
        mode.takeUserInputData()
        print(mode.userGender, mode.userAge, mode.userHeight, mode.userWeight, mode.userLevelOfActivity, mode.userGoal, mode.userTime)
        mode.calculateTDEE()
        print(mode.userTDEE)
        ''' # THE FOLLOWING CODE GOES MORE INTO ABOUT THE WEIGHT LOSS AND CALORIE DEFICIT RESTRICTIONS
        mode.caloriesToLosePerDay = 3500 * (mode.userWeight - mode.userGoal) / mode.userTime
        print(mode.caloriesToLosePerDay)
        if mode.caloriesToLosePerDay > 1000:
            mode.daysMin = 3500 * (mode.userWeight - mode.userGoal) / 1000
            mode.daysMax = 3500 * (mode.userWeight - mode.userGoal) / 500
            print("Realistically, you should try to lose this weight in", mode.daysMin, "to", mode.daysMax, "days.")
        else:
            print("You need to eat about", mode.caloriesToLosePerDay, "less calories per day!")'''
        mode.userFoodDict = dict()

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
        mode.userLevelOfActivity = mode.getUserInput("Rate your level of activity based on these scales:\n 1 = Sedentary (little to no exercise)\n 2 = Lightly Active (light exercise 1-3 days / week)\n 3 = Moderately Active (moderate exercise 3-5 days / week)\n 4 = Very Active (heavy exercise 6-7 days / week)\n 5 = Extremely Active (very heavy exercise, hard labor job, training 2x / day)")
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

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)
    
    def mousePressed(mode, event):      
        # search food drink
        if (0 <= event.x <= 200) and (0 <= event.y <= 250):
            userinput = mode.getUserInput("What did you eat or drink today? ")
            if (userinput == None) or len(userinput) == 0:
                pass
            else:
                mode.getFoodDict(userinput) 
        # check user list
        elif ((0 <= event.x <= 200) and (250 < event.y <= 500)) and len(mode.userFoodDict) > 0:
            mode.app.setActiveMode(mode.app.userList)
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
                    mode.quantity = int(mode.getUserInput("How many servings?"))
                    mode.userFoodDict[newFoodCoord] = mode.foodFullDict[newFoodCoord] + [mode.quantity] + [(mode.quantity * mode.foodFullDict[newFoodCoord][0][0], mode.quantity * mode.foodFullDict[newFoodCoord][0][1], mode.quantity * mode.foodFullDict[newFoodCoord][0][2])]
                    print(mode.userFoodDict)

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
                canvas.create_text(300, mode.foodFullDict[foodname][2], text=foodname, font='Calibri 13 bold',anchor='w')
                canvas.create_text(300, mode.foodFullDict[foodname][2] + 20, text=f'Carbs (g): {mode.foodFullDict[foodname][0][0]}', anchor='w')
                canvas.create_text(400, mode.foodFullDict[foodname][2] + 20, text=f'Proteins (g): {mode.foodFullDict[foodname][0][1]}', anchor='w')
                canvas.create_text(500, mode.foodFullDict[foodname][2] + 20, text=f'Fats (g): {mode.foodFullDict[foodname][0][2]}', anchor='w')
                # separate foods with lines
                canvas.create_line(200, mode.foodFullDict[foodname][2] + 37.5, mode.width, mode.foodFullDict[foodname][2] + 37.5)
                # add-to-list button
                canvas.create_rectangle(575, mode.foodFullDict[foodname][2] + 20, 650, mode.foodFullDict[foodname][2] + 35, fill='cyan')
                canvas.create_text(612.5, mode.foodFullDict[foodname][2] + 27.5, text='Add to List')

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
                mode.foodFullDict[foodname] = (carbContent, proteinContent, fatContent)

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

        print(mode.foodFullDict) # final food dict with macros + image url
    
    def redrawAll(mode, canvas):
        canvas.create_line(200, 0, 200, mode.height)     
        canvas.create_rectangle(0, 0, 200, 250, fill='red')
        canvas.create_text(100, 125, text='Search Food / Drink', font='Calibri 15 bold')
        canvas.create_rectangle(0, 250, 200, 500, fill='yellow')
        canvas.create_text(100, 375, text='Check Current User List', font='Calibri 15 bold')
        canvas.create_rectangle(0, 500, 200, 750, fill='green')
        canvas.create_text(100, 625, text='See Results', font='Calibri 15 bold')    
        mode.displayFoods(canvas)

class UserFoodsList(SandboxMode):
    def appStarted(mode):
        pass

    def keyPressed(mode, event):
        pass

    def mousePressed(mode, event):
        pass

    def displayUserFoods(mode, canvas):
        pass

    def redrawAll(mode, canvas):
        pass


class Results(SandboxMode):
    def appStarted(mode):
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)
    
    def redrawAll(mode, canvas):
        # if mode.results:
        #     data1 = {'Macronutrients': ['CARB', 'PROT', 'FATS'],
        #     'Percentage of Diet': [0.25, 0.25, 0.50]
        #     }
        #     df1 = DataFrame(data1,columns=['Macronutrients','Percentage of Diet'])
            
        #     figure1 = plt.Figure(figsize=(7,5), dpi=100)
        #     ax1 = figure1.add_subplot(111)
        #     bar1 = FigureCanvasTkAgg(figure1, canvas)
        #     bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        #     df1 = df1[['Macronutrients','Percentage of Diet']].groupby('Macronutrients').sum()

        #     df1.plot(kind='bar', legend=True, ax=ax1, color=['red', 'blue', 'green'])
        #     ax1.set_title('Macronutrients Vs. Percentage of Diet')
        pass

class PuzzleMode(Mode):
    def appStarted(mode):
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

class Instructions(Mode):
    def appStarted(mode):
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)
    
    def redrawAll(mode, canvas):
        pass

class Credits(Mode):
    def appStarted(mode):
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

class HelpMode(Mode):
    def appStarted(mode):
        url = 'https://i.pinimg.com/originals/fe/f7/2f/fef72f73f4f961b4ed6f8e4bb093eb1b.jpg'
        mode.appIcon = mode.loadImage(url)
        mode.appIcon2 = mode.scaleImage(mode.appIcon, 1/3)

    def redrawAll(mode, canvas):
        font = 'Courier 20 bold'
        canvas.create_image(250, 250, image=ImageTk.PhotoImage(mode.appIcon2))
        canvas.create_text(mode.width/2, 75, text='Instructions', font=font)
        canvas.create_text(mode.width/2, 150, text='This is the help screen!', font=font)
        canvas.create_text(mode.width/2, 250, text='(Insert helpful message here)', font=font)
        canvas.create_text(mode.width/2, 350, text='Press any key to return to the game!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.sandboxMode = SandboxMode()
        app.userList = UserFoodsList()
        app.resultsMode = Results()
        app.puzzleMode = PuzzleMode()
        app.instructions = Instructions()
        app.credits = Credits()
        # app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=650, height=750)
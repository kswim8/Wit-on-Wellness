# This Sandbox Mode is used for user freedom to experiment with different diets
# and food/meal plans. They can also receive feedback and results on the meal plan
# based on goals that they input at the beginning of using Sandbox.

# CITATION: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#subclassingModalApp 
# CITATION: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#cachingPhotoImages
from cmu_112_graphics import *
import random, requests, bs4, json, nltk
nltk.download('brown')
from nltk.corpus import wordnet as wn
from nltk.corpus import brown

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
    userinput1 = userinput2 = userinput3 = userinput4 = userinput5 = userinput6 = userinput7 = userinput8 = None

    def appStarted(mode):
        mode.results = False
        mode.foodentered = False
        mode.userList = False
        mode.userProfile = False
        mode.userFoodDict = dict()
        mode.userfoodcounter = 0
        mode.userGender = mode.userAge = mode.userHeight = mode.userWeight = mode.userLevelOfActivity = mode.userGoal = mode.userTime = mode.userGoal2 = None
        mode.importedData = False
        mode.exportedData = False
        mode.autocompletionResults = False

    def takeUserInputData(mode):
        # CITATION: https://steelfitusa.com/2018/10/calculate-tdee/
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
    
    def importData(mode):
        try:
            # reading the file
            # CITATION: https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/
            f = open("userdata.txt", "r")
            result = f.read()
            userData = []
            # appending each item to a list to be processed
            for item in result.split("~"):
                userData += [item]
            print(userData)

            # setting the list items equal to their mode.variables
            mode.userGender = userData[0]
            mode.userAge = int(userData[1])
            mode.userHeight = int(userData[2])
            mode.userWeight = int(userData[3])
            mode.userLevelOfActivity = int(userData[4])
            mode.userGoal = int(userData[5])
            mode.userTime = int(userData[6])
            mode.userGoal2 = int(userData[7])
            if len(userData) > 8:
                # CITATION: https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/
                mode.userFoodDict = json.loads(userData[8])

            # calculating all the values needed for results
            mode.calculateTDEE()
            for foodname in mode.userFoodDict:
                SandboxMode.totalCarbs += mode.userFoodDict[foodname][4][0]
                SandboxMode.totalProtein += mode.userFoodDict[foodname][4][1]
                SandboxMode.totalFat += mode.userFoodDict[foodname][4][2]
                SandboxMode.totalCalories = SandboxMode.totalCarbs * 4 + SandboxMode.totalProtein * 4 + SandboxMode.totalFat * 9

            SandboxMode.userCurrentWeight = mode.userWeight
            SandboxMode.userDesiredWeight = mode.userGoal
            SandboxMode.userTimeExpected = mode.userTime
            SandboxMode.userGoal = mode.userGoal2
            mode.userfoodcounter = len(mode.userFoodDict)
            mode.importedData = True
        except:
            f = open("userdata.txt", "w")
            result = str('M') + "~" + str(20) + "~" + str(60) + "~" + str(155) + "~" + str(3) + "~" + str(150) + "~" + str(30) + "~" + str(3)
            f.write(result)

    def exportData(mode):
        # creating the text file for the userdata
        # CITATION: https://www.geeksforgeeks.org/python-convert-dictionary-object-into-string/
        if mode.userGender != None:
            f = open("userdata.txt", "w")
            result = str(mode.userGender) + "~" + str(mode.userAge) + "~" + str(mode.userHeight) + "~" + str(mode.userWeight) + "~" + str(mode.userLevelOfActivity) + "~" + str(mode.userGoal) + "~" + str(mode.userTime) + "~" + str(mode.userGoal2)
            if mode.userFoodDict != {}:
                # CITATION: https://www.geeksforgeeks.org/python-convert-dictionary-object-into-string/
                result = result + "~" + json.dumps(mode.userFoodDict)
            f.write(result)
            print(result)
            mode.exportedData = True
        else:
            print("Nothing exported.")
            pass

    def mouseMoved(mode, event):
        if not mode.userList:
            if (0 <= event.x <= 200) and (625 < event.y <= 750): # View User Profile
                mode.userProfile = True
            else:
                mode.userProfile = False

    def mousePressed(mode, event):
        if not mode.userList:      
            # search food drink
            if (0 <= event.x <= 200):
                if (0 <= event.y <= 125): # Enter User Data
                    mode.takeUserInputData()
                    mode.calculateTDEE()
                elif (125 < event.y <= 250): # Search Food / Drink
                    userinput = mode.getUserInput("What did you eat or drink today? ")
                    if (userinput == None) or len(userinput) == 0:
                        pass
                    else:
                        mode.getFoodDict(userinput) 
                elif (250 < event.y <= 375): # Check Current User List
                    mode.userList = True
                elif (375 < event.y <= 500): # See Results
                    mode.results = not mode.results
                    mode.app.setActiveMode(mode.app.resultsMode)
                elif (500 < event.y <= 625):
                    if (0 <= event.x < 100): # Import Data
                        mode.importData()
                    elif (100 <= event.x <= 200): # Export Data
                        mode.exportData()

            # add to list buttons
            if (mode.foodentered):
                mode.foodselected = False

                if mode.autocompletionResults:
                    if (200 <= event.x <= 650):
                        clickedarea = int(event.y / 37.5)
                        # print(mode.matchingFoodsList[clickedarea])
                        # print(type(mode.matchingFoodsList[clickedarea]))
                        mode.getFoodDict(mode.matchingFoodsList[clickedarea][0])
                        mode.autocompletionResults = False

                else:
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
            elif mode.userFoodDict != {} and mode.userGender == None:
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

    def displayAutoCompletion(mode, canvas):
        for i in range(len(mode.matchingFoodsList)):
            canvas.create_text(mode.width/2, mode.matchingFoodsList[i][2], text=mode.matchingFoodsList[i][0], anchor='w')
            canvas.create_line(200, mode.matchingFoodsList[i][2] + 18.75, mode.width, mode.matchingFoodsList[i][2] + 18.75)

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
        mode.matchingFoodsList = []
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
                # print(response.json())
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
                # CITATION: https://stackoverflow.com/questions/19626737/where-can-i-find-a-text-list-or-library-that-contains-a-list-of-common-foods
                # using the corpus for food to get autocompletion results
                food = wn.synset('food.n.02')
                foodcorpus = (set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))
                # CITATION: https://stackoverflow.com/questions/7764229/sort-words-by-their-usage
                # using the brown corpus to find the popularity/usage of a word to sort the autocompletion results
                freqs = nltk.FreqDist(w.lower() for w in brown.words()) # how the frequencies are calculated
                mode.matchingFoodsList = []
                mode.autocompleteresultscounter = 18.75
                try:
                    for thefoods in foodcorpus:
                        if thefoods.startswith(userinput):
                            thefoods = thefoods.replace('_', ' ') # the foods have underscores, which make it hard to feed back into API so replace
                            mode.matchingFoodsList.append([thefoods, freqs[thefoods]]) # each food is a list of [name, frequency]
                        if len(mode.matchingFoodsList) >= 20:
                            break 
                    mode.matchingFoodsList2 = []
                    # CITATION: https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
                    # the scoring by popularity is done here, where it sorts from least to greatest
                    mode.matchingFoodsList = sorted(mode.matchingFoodsList, key=lambda x: x[1]) # this is the line where the scoring is sorted

                    # since least to greatest, it needs to be reversed
                    for item in reversed(mode.matchingFoodsList): 
                        mode.matchingFoodsList2.append(item)
                    
                    mode.matchingFoodsList = mode.matchingFoodsList2

                    # print(mode.matchingFoodsList)

                    # embedding the coordinates for the autocomplete
                    for i in range(len(mode.matchingFoodsList)):
                        mode.matchingFoodsList[i].append(mode.autocompleteresultscounter)
                        mode.autocompleteresultscounter += 37.5

                    mode.autocompletionResults = True
                    mode.displayAutoCompletion(canvas)
                except:
                    # displaying autocompletion results if there is a returned list
                    if len(mode.matchingFoodsList) > 0: 
                        mode.app.showMessage(f"Could not find a food or drink labeled {userinput}, please try one of the autocompletions.")
                    # no matches, not even with autocomplete
                    else:
                        mode.app.showMessage(f"Could not find a food or drink labeled {userinput}, please try a different query.")

        # CITATION: https://stackoverflow.com/questions/21530274/format-for-a-url-that-goes-to-google-image-search
        # web scrape for the image from google images
        mode.picCy = 25 # embed the locations of where they will be placed using mode.picCy
        for foodname in foodset:
            try:
                # CITATION: It is infeasible to cite every image here because the web scraping and photo used is determined by user input, which has millions of possibilities.
                # To explain this part of the code, I webscrape from Google Images and take the first image every time for each listed food returned by the API (in foodset)
                imagerequest = requests.get(f'https://www.google.com/search?tbm=isch&q={foodname}%20food%20or%20drink')
                soup = bs4.BeautifulSoup(imagerequest.text, 'html.parser')
                firstimage = soup.find_all("img")[1]    # i put this somewhere else too, but this is the first image on google (0 index is google logo)
                firstimage = str(firstimage)            # type cast to string for easier parsing, since it's an html tag when using bs4
                srcindex = firstimage.find('http')      # parsing for start of link
                foodimageurl = firstimage[srcindex:-3]  # slicing for url of image   
                # print("THE DICT:", mode.foodFullDict[foodname])
                # print("THE IMAGE URL:", firstimage[srcindex:-3])
                # print("THE FOODNAME:", foodname)
                mode.foodFullDict[foodname] = [mode.foodFullDict[foodname], firstimage[srcindex:-3], mode.picCy] # assign value to key
                mode.foodFullDictCoords[foodname] = mode.picCy
                mode.picCy += 75   
            except:
                pass 

        # print(mode.foodFullDict) # final food dict with macros + image url

    def redrawAll(mode, canvas):
        if not mode.userList:
            canvas.create_line(200, 0, 200, mode.height)     
            canvas.create_rectangle(0, 0, 200, 125, fill='red')
            canvas.create_text(100, 62.5, text='Enter User Data', font='Calibri 15 bold')
            canvas.create_rectangle(0, 125, 200, 250, fill='orange')
            canvas.create_text(100, 187.5, text='Search Food / Drink', font='Calibri 15 bold')
            canvas.create_rectangle(0, 250, 200, 375, fill='yellow')
            canvas.create_text(100, 312.5, text='Check Current User List', font='Calibri 15 bold')      
            canvas.create_rectangle(0, 375, 200, 500, fill='green')
            canvas.create_text(100, 437.5, text='See Results', font='Calibri 15 bold')
            canvas.create_rectangle(0, 500, 200, 625, fill='blue')
            canvas.create_line(100, 500, 100, 625) # creating import export in same box
            canvas.create_text(50, 562.5, text='Import\nData', font='Calibri 15 bold')
            canvas.create_text(150, 562.5, text='Export\nData', font='Calibri 15 bold')
            canvas.create_rectangle(0, 625, 200, 750, fill='purple')
            canvas.create_text(100, 687.5, text='View User Profile', font='Calibri 15 bold')  
            
            if mode.autocompletionResults:
                mode.displayAutoCompletion(canvas)

            mode.displayFoods(canvas)
            '''
            if mode.importedData:
                canvas.create_rectangle()
                canvas.create_text()

            if mode.exportedData:
                canvas.create_rectangle()
                canvas.create_text()
            '''
            if mode.userProfile:
                canvas.create_rectangle(205, 475, 525, 745, fill='white', width=5)
                if mode.userGender != None:
                    if mode.userGoal2 == 1: mode.userGoal2Text = 'Lose fat'
                    elif mode.userGoal2 == 2: mode.userGoal2Text = 'Build muscle'
                    elif mode.userGoal2 == 3: mode.userGoal2Text = 'Balanced diet'
                    if mode.userGender == 'm' or mode.userGender == 'M': mode.userGenderText = 'Male'
                    elif mode.userGender == 'f' or mode.userGender == 'F': mode.userGenderText = 'Fenale'
                    canvas.create_text(265, 500, text='User Profile', font='Calibri 20 bold', anchor='w')
                    canvas.create_text(265, 620, text=f'Gender: {mode.userGenderText}\nAge: {mode.userAge}\nHeight: {mode.userHeight} in\nWeight: {mode.userWeight} lbs\nLevel of Activity: {mode.userLevelOfActivity}\nGoal Weight: {mode.userGoal} lbs\nTime Expected: {mode.userTime} days\nUser Goal: {mode.userGoal2Text}', font='Calibri 14 bold', anchor='w')
                else:
                    canvas.create_text(265, 560, text='No profile made yet.', font='Calibri 14 bold', anchor='w')
            

        elif mode.userList:
            if mode.userFoodDict == {}: 
                canvas.create_text(mode.width/2, mode.height/2, text='You have no foods or drinks in your list.', font='Calibri 15 bold')
                canvas.create_rectangle(mode.width/2 - 200, mode.height/2 + 100, mode.width/2 + 200, mode.height/2 + 200, fill='cyan')
                canvas.create_text(mode.width/2, mode.height/2 + 150, text='Go Back to Search & Add Food / Drinks', font='Calibri 12 bold')
            else:
                canvas.create_text(5, 25, text='User List of Foods / Drinks', font='Calibri 15 bold', anchor='w')
                canvas.create_line(0, 50, mode.width, 50)
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
        if SandboxMode.totalCalories == 0 or SandboxMode.userCurrentWeight == None:
            if (mode.width/2 - 100 <= event.x <= mode.width/2 + 100) and (mode.height/2 + 100 <= event.y <= mode.height/2 + 300):
                mode.app.setActiveMode(mode.app.sandboxMode)
        pass

    def mouseMoved(mode, event):
        # show the exact percentage over the bar and a message about the macro itself in relation to user goal
        if SandboxMode.totalCalories != 0 and SandboxMode.userCurrentWeight != None:
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
        # print(mode.carbsProportion, mode.proteinProportion, mode.fatProportion)
    
    def checkProportions(mode):
        # check for user's goal (lose fat, build muscle, etc.)
        # return a tuple of bar colors and bar heights
        # print(SandboxMode.userGoal)
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

        # balanced diet (this was purely based on my own intuition and my friend's)
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

        # text advice: the following text is all based on the calculations
        # I cited the suggestions from where I got my information
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

        # CITATION: https://www.healthline.com/nutrition/how-to-lose-weight-as-fast-as-possible#:~:text=The%20first%20week%20is%20usually,is%20usually%20a%20safe%20amount.
        # (explains why it's safer and healthier to lose weight in increments of 1-2 lbs a week)

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
                    canvas.create_text(638, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
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
                    canvas.create_text(638, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
                    canvas.create_line(390, 183, 640, 266)
                    if SandboxMode.totalCalories > SandboxMode.userTDEE - mode.caloriesToLosePerDay:
                        canvas.create_text(380, 450, text='You need to eat about\n%0.1f less calories per day\nto reach your goal.' % (SandboxMode.totalCalories - SandboxMode.userTDEE - mode.caloriesToLosePerDay), anchor='w', font='Calibri 12')
                    elif SandboxMode.totalCalories < SandboxMode.userTDEE - mode.caloriesToLosePerDay:
                        canvas.create_text(380, 450, text='You need to eat about\n%0.1f more calories per day\nto reach your goal.' % (SandboxMode.userTDEE - SandboxMode.totalCalories - mode.caloriesToLosePerDay), anchor='w', font='Calibri 12')
                    canvas.create_text(380, 525, text='This means eating about\n%0.1f calories per day while\nexercising consistently!' % (SandboxMode.userTDEE - mode.caloriesToLosePerDay), anchor='w', font='Calibri 12')
                    # print("You need to eat about", mode.caloriesToLosePerDay, "less calories per day to reach your goal.")
                    # print("This means eating about", (SandboxMode.userTDEE - mode.caloriesToLosePerDay), "calories per day while exercising consistently!")
            elif SandboxMode.userCurrentWeight < SandboxMode.userDesiredWeight:
                mode.caloriesToGainPerDay = 3500 * (SandboxMode.userDesiredWeight - SandboxMode.userCurrentWeight) / SandboxMode.userTimeExpected
                # print(mode.caloriesToGainPerDay)
                if mode.caloriesToGainPerDay > 1000:
                    mode.daysMin = 3500 * (SandboxMode.userDesiredWeight - SandboxMode.userCurrentWeight) / 1000
                    mode.daysMax = 3500 * (SandboxMode.userDesiredWeight - SandboxMode.userCurrentWeight) / 500
                    canvas.create_text(380, 183, text=SandboxMode.userDesiredWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_text(380, 266, text=SandboxMode.userCurrentWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_text(515, 367, text='%0.1f' % mode.daysMin, font='Calibri 10 bold') # min days
                    canvas.create_text(638, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
                    canvas.create_line(390, 266, 640, 183)
                    canvas.create_text(380, 450, text='Realistically, you should try to\ngain this weight in %0.1f to\n%0.1f days.' % (mode.daysMin, mode.daysMax), anchor='w')
                    canvas.create_text(380, 525, text='This means still eating at least\n%0.1f and at most %0.1f calories\nper day while exercising consistently\nfor healthy weight gain!' % (SandboxMode.userTDEE + 500, SandboxMode.userTDEE + 1000), anchor='w', font='Calibri 12')
                    # print("Realistically, you should try to gain this weight in", mode.daysMin, "to", mode.daysMax, "days.")
                    # print("This means eating at most", (SandboxMode.userTDEE - 1000), "calories per day while exercising consistently for healthy weight gain!")
                else:
                    mode.daysMax = SandboxMode.userTimeExpected
                    canvas.create_text(380, 183, text=SandboxMode.userDesiredWeight, anchor='e', font='Calibri 10 bold') 
                    canvas.create_text(380, 266, text=SandboxMode.userCurrentWeight, anchor='e', font='Calibri 10 bold')
                    canvas.create_text(638, 367, text='%0.1f' % mode.daysMax, font='Calibri 10 bold') # max days
                    canvas.create_line(390, 266, 640, 183)
                    if SandboxMode.totalCalories > SandboxMode.userTDEE + mode.caloriesToGainPerDay:
                        canvas.create_text(380, 450, text='You need to eat about\n%0.1f less calories per day\nto reach your goal.' % (SandboxMode.totalCalories - SandboxMode.userTDEE + mode.caloriesToGainPerDay), anchor='w', font='Calibri 12')
                    elif SandboxMode.totalCalories < SandboxMode.userTDEE + mode.caloriesToGainPerDay:
                        canvas.create_text(380, 450, text='You need to eat about\n%0.1f more calories per day\nto reach your goal.' % (SandboxMode.userTDEE - SandboxMode.totalCalories + mode.caloriesToGainPerDay), anchor='w', font='Calibri 12')
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

        canvas.create_text(380, 600, text='User Calories: %0.2f calories' % SandboxMode.totalCalories, font='Calibri 12 bold', anchor='w') # total Calories
        canvas.create_text(380, 630, text='TDEE: %0.2f calories' % SandboxMode.userTDEE, font='Calibri 12 bold', anchor='w') # tdee
        # CITATION: https://tdeecalculator.net/ (What is TDEE?)
        canvas.create_text(380, 685, text='TDEE (Total daily energy expenditure):\nhow many calories you are expected to burn.\nUsing this value, we can find how many more\nor less calories should be consumed to\ngain or lose weight. ', anchor='w')
    
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, 40, fill='cyan')
        canvas.create_text(mode.width/2, 20, text='Results', font='Calibri 15 bold')
        # if there is not enough data to work with, then no results
        if SandboxMode.totalCalories == 0 or SandboxMode.userCurrentWeight == None:
            canvas.create_text(mode.width/2, mode.height/2, text='No results to show.', font='Calibri 15 bold')
            canvas.create_rectangle(mode.width/2 - 100, mode.height/2 + 150, mode.width/2 + 100, mode.height/2 + 250, fill='cyan')
            canvas.create_text(mode.width/2, mode.height/2 + 200, text='Go Back to Sandbox', font='Calibri 15 bold')
        # enough data, report results through visuals and such
        else:
            canvas.create_line(mode.width/2, 40, mode.width/2, mode.height)
            mode.findProportions()
            mode.drawBarGraph(canvas)
            mode.drawLinePlot(canvas)

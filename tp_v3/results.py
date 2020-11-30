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

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
        mode.appIcon2 = mode.scaleImage(mode.appIcon, 1/3)
    
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
        font = 'Calibri 26 bold'
        canvas.create_image(mode.width/2, mode.height/2, image=ImageTk.PhotoImage(mode.appIcon2))
        canvas.create_text(mode.width/2, mode.height/2-175, text='Wit on Wellness', font=font)
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
        # mode.showMessage("For results, please answer all the following questions truthfully.")
        # mode.userGender = mode.getUserInput("What is your biological gender (M/F) ?")
        # while True:
        #     if mode.userGender == None or (mode.userGender).upper() != 'M' and (mode.userGender).upper() != 'F':
        #         mode.userGender = mode.getUserInput("What is your biological gender (M/F) ?")
        #     else:
        #         break
        # mode.userAge = mode.getUserInput("How old are you in years?")
        # while True:
        #     if mode.userAge == None or not (mode.userAge).isdigit() or int(mode.userAge) > 120 or int(mode.userAge) < 0:
        #         mode.userAge = mode.getUserInput("How old are you in years?")
        #     else:
        #         mode.userAge = int(mode.userAge)
        #         break
        # mode.userHeight = mode.getUserInput("What is your height in centimeters?")
        # while True:
        #     if mode.userHeight == None or not (mode.userHeight).isdigit() or int(mode.userHeight) > 300 or int(mode.userHeight) < 0:
        #         mode.userAge = mode.getUserInput("What is your height in centimeters?")
        #     else:
        #         mode.userHeight = int(mode.userHeight)
        #         break
        # mode.userWeight = mode.getUserInput("What is your weight in kilograms?")
        # while True:
        #     if mode.userWeight == None or not (mode.userWeight).isdigit() or int(mode.userWeight) > 650 or int(mode.userWeight) < 0:
        #         mode.userAge = mode.getUserInput("What is your weight in kilograms?")
        #     else:
        #         mode.userWeight = int(mode.userWeight)
        #         break
        # mode.userLevelOfActivity = mode.getUserInput("Rate your level of activity:")
        # print(mode.userGender,mode.userAge,mode.userHeight, mode.userWeight,mode.userLevelOfActivity)
        mode.results = False
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)
    
    def mousePressed(mode, event):
        if (0 <= event.x <= 100) and (0 <= event.y <= 50):
            mode.results = not mode.results
    
    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, 100, 50)
        canvas.create_text(50, 25, text='See Results')
        if mode.results:
            data1 = {'Macronutrients': ['CARB', 'PROT', 'FATS'],
            'Percentage of Diet': [0.33, 0.67, 1.00] # data for bar height
            }
            df1 = DataFrame(data1,columns=['Macronutrients','Percentage of Diet'])
            
            figure1 = plt.Figure(figsize=(7,4), dpi=100)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, canvas)
            bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df1 = df1[['Macronutrients','Percentage of Diet']].groupby('Macronutrients').sum()
            df1.plot(kind='bar', legend=True, ax=ax1)
            ax1.set_title('Macronutrients Vs. Percentage of Diet')

        pass

class Results(SandboxMode):
    def appStarted(mode):
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)
    
    def redrawAll(mode, canvas):
        data1 = {'Macronutrients': ['CARB', 'PROT', 'FATS'],
         'Percentage of Diet': [0.25, 0.25, 0.50]
        }
        df1 = DataFrame(data1,columns=['Macronutrients','Percentage of Diet'])
        
        figure1 = plt.Figure(figsize=(7,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, canvas)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df1 = df1[['Macronutrients','Percentage of Diet']].groupby('Macronutrients').sum()

        df1.plot(kind='bar', legend=True, ax=ax1, color=['red', 'blue', 'green'])
        ax1.set_title('Macronutrients Vs. Percentage of Diet')

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

class GameMode(Mode):
    def appStarted(mode):
        mode.score = 0
        mode.randomizeDot()

    def randomizeDot(mode):
        mode.x = random.randint(20, mode.width-20)
        mode.y = random.randint(20, mode.height-20)
        mode.r = random.randint(10, 20)
        mode.color = random.choice(['red', 'orange', 'yellow', 'green', 'blue'])
        mode.dx = random.choice([+1,-1])*random.randint(3,6)
        mode.dy = random.choice([+1,-1])*random.randint(3,6)

    def moveDot(mode):
        mode.x += mode.dx
        if (mode.x < 0) or (mode.x > mode.width): mode.dx = -mode.dx
        mode.y += mode.dy
        if (mode.y < 0) or (mode.y > mode.height): mode.dy = -mode.dy

    def timerFired(mode):
        mode.moveDot()

    def mousePressed(mode, event):
        d = ((mode.x - event.x)**2 + (mode.y - event.y)**2)**0.5
        if (d <= mode.r):
            mode.score += 1
            mode.randomizeDot()
        elif (mode.score > 0):
            mode.score -= 1

    def keyPressed(mode, event):
        if (event.key == 'h'):
            mode.app.setActiveMode(mode.app.helpMode)

    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 20, text=f'Score: {mode.score}', font=font)
        canvas.create_text(mode.width/2, 50, text='Click on the dot!', font=font)
        canvas.create_text(mode.width/2, 80, text='Press h for help screen!', font=font)
        canvas.create_oval(mode.x-mode.r, mode.y-mode.r, mode.x+mode.r, mode.y+mode.r,
                           fill=mode.color)

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
        app.puzzleMode = PuzzleMode()
        app.instructions = Instructions()
        app.credits = Credits()
        # app.gameMode = GameMode()
        # app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=650, height=500)
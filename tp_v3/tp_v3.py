# Keren Huang Term Project

import module_manager
module_manager.review()
from cmu_112_graphics import *
import random, requests, bs4, json
from splashscreen import *
from sandbox import *

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
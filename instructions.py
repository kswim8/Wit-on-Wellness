# This is the Instructions page, which is linked to the other modes as well.
# It mainly describes each mode while showing screenshots of the modes.

from cmu_112_graphics import *
import random, requests, bs4, json

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

from cmu_112_graphics import *
import random, requests, bs4, json

class SplashScreenMode(Mode):
    def appStarted(mode):
        # CITATION: https://i.pinimg.com/originals/fe/f7/2f/fef72f73f4f961b4ed6f8e4bb093eb1b.jpg
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

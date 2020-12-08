# This is the landing and splash screen for the app, where the user can pick their path.
# There are options for Sandbox, Puzzle Mode, or Instructions if they would like.

# CITATION: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#subclassingModalApp 
from cmu_112_graphics import *
import random, requests, bs4, json

class AIChatBot(Mode):
    def appStarted(mode):
        # CITATION: This is the background photo
        url = 'https://i.pinimg.com/originals/fe/f7/2f/fef72f73f4f961b4ed6f8e4bb093eb1b.jpg'
        mode.appIcon = mode.loadImage(url)
        mode.appIcon2 = mode.scaleImage(mode.appIcon, 4.5/10)
        # CITATION: https://cooltext.com/Logo-Design-Gold-Outline
        # This was how I created and imported my title font lol
        mode.appTitle = mode.loadImage('splashscreentitle.png')

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2, image=ImageTk.PhotoImage(mode.appIcon2))
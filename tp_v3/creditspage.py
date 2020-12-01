from cmu_112_graphics import *
import random, requests, bs4, json

class Credits(Mode):
    def appStarted(mode):
        pass

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

    def redrawAll(mode, canvas):
        # canvas.create_text(mode.width/2, mode.height/2, text='Keren Huang\nMentor: Alex Xie')
        pass
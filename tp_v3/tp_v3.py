# Keren Huang Term Project

import module_manager
module_manager.review()
from cmu_112_graphics import *
import random, requests, bs4, json
from splashscreen import *
from instructions import *
from sandbox import *
from puzzlemode import *

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
# Keren Huang Term Project

# CITATION: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#subclassingModalApp
# CITATION: https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#installingModules

import module_manager
module_manager.review()
from cmu_112_graphics import *
import random, requests, bs4, json
from splashscreen import *
from instructions import *
from sandbox import *
from puzzlemode import *
from creditspage import *

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.sandboxMode = SandboxMode()
        app.resultsMode = Results()
        app.puzzleMode = PuzzleMode()
        app.puzzleMode1 = PuzzleMode1()
        app.puzzleMode2 = PuzzleMode2()
        app.chickfilaMenu = ChickFilA()
        app.mcdonaldsMenu = McDonalds()
        app.instructions = Instructions()
        app.credits = Credits()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=650, height=750)
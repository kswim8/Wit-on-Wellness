# Keren Huang's (kerenh) Term Project
# Idea: Health Simulator
# Steps:
# 1. splash screen with epic design, welcome the user
# 2. take user input for height / weight
# 3. provide UI with buttons to perform activities
# 4. FDA has data on food and nutrition
# 5. if JSON or XML, extract data from website using API 
# 6. add animations for the activities
# 7. provide advice or data on deficiencies
# 8. allow userse to repeat process to simulating 

from cmu_112_graphics import *
import module_manager
module_manager.review()

# primary function to run app
def playHealthSimulator(app):
    
    pass

def appStarted(app):
    app.firstStart = True
    app.userInfoScreen = False

def mousePressed(app, event):
    if app.firstStart:
        app.firstStart = False
        app.userInfoScreen = True

# step 1. create splash screen
def drawSplashScreen(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text="Health Simulator", font="Times 12 bold")

def drawUserInfoScreen(app, canvas):
    canvas.create_text(app.width/2, app.height/2, text="Enter your height:", font="Times 12 bold")
    pass

# drawing all the pages and components
def redrawAll(app, canvas):
    if app.firstStart:
        drawSplashScreen(app, canvas)
    else:
        playHealthSimulator(app)
        if app.userInfoScreen:
            drawUserInfoScreen(app, canvas)

runApp(width=500, height=500)
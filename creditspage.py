from cmu_112_graphics import *
import random, requests, bs4, json

class Credits(Mode):
    def appStarted(mode):
        kerenpic = 'https://i.imgur.com/C5KDwXl.png'
        alexpic = 'https://www.cs.cmu.edu/~112/staff-photos/alexx.jpg'
        mode.kerenPic = mode.loadImage(kerenpic)
        mode.kerenPic2 = mode.scaleImage(mode.kerenPic, 1)
        mode.alexPic = mode.loadImage(alexpic)
        mode.alexPic2 = mode.scaleImage(mode.alexPic, 1)

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

    def redrawAll(mode, canvas):
        canvas.create_text(mode.width/2, 50, text='Credits', font='Calibri 20 bold')
        canvas.create_text(mode.width/2, mode.height/2, text='Keren Huang\nMentor: Alex Xie')
        canvas.create_image(mode.width/4, mode.height/2, image=ImageTk.PhotoImage(mode.kerenPic2))
        canvas.create_image(3*mode.width/4, mode.height/2, image=ImageTk.PhotoImage(mode.alexPic2))
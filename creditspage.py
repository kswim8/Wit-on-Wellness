# This is a page where you can enjoy pictures of me and Alex who helped to make this app.

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
        url = 'https://i.pinimg.com/originals/fe/f7/2f/fef72f73f4f961b4ed6f8e4bb093eb1b.jpg'
        mode.appIcon = mode.loadImage(url)
        mode.appIcon2 = mode.scaleImage(mode.appIcon, 4.5/10)

    def keyPressed(mode, event):
        if (event.key == 'Escape'):
            mode.app.setActiveMode(mode.app.splashScreenMode)

    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2, image=ImageTk.PhotoImage(mode.appIcon2))
        canvas.create_text(mode.width/2, 50, text='Credits', font='Calibri 20 bold')
        canvas.create_text(mode.width/2, mode.height - 100, text='Keren Huang | Mentor: Alex Xie', font='Calibri 15 bold')
        canvas.create_image(mode.width/4, mode.height/2, image=ImageTk.PhotoImage(mode.kerenPic2))
        canvas.create_image(3*mode.width/4, mode.height/2, image=ImageTk.PhotoImage(mode.alexPic2))
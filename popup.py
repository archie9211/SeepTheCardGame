import sys
from tkinter import *
import webbrowser
ABOUT_TEXT = """
Introduction of rules
"""
def callbackrules():
    webbrowser.open_new(r"rules url ")
def rules():
    toplevel = Toplevel()
    labelx= Label(toplevel, text=ABOUT_TEXT, height=0, width=100)
    toplevel.title("RULES")
    ebutton9 = Button(toplevel, text="Read Rules", command=callbackrules)
    ebutton9.pack(fill=BOTH)
    labelx.pack()
def showError(string):
    toplevel1=Toplevel()
    labelz= Label(toplevel1, text=string, height=0, width=100)
    toplevel1.title("Popup")
    labelz.pack()

WARNING="""Are You Sure!!!"""
def quit():
    import os
    os._exit(1)

def exitOption():
    exitWindow=Toplevel()
    exitWindow.title("Exit")
    exitWindow.geometry("300x100")
    warning=Label(exitWindow,text=WARNING)
    warning.pack(side="top")
    yesButton=Button(exitWindow,text="YES",command=quit)
    yesButton.pack(expand=YES,side="left")
    noButton=Button(exitWindow,text="No",command=exitWindow.destroy )
    noButton.pack(expand=YES,side="right")


def callbacksumit():
    webbrowser.open_new(r"https://www.facebook.com/sumit.kumardaroch")


def callbacknitin():
    webbrowser.open_new(r"https://www.facebook.com/nd.nitin.dogra")


def callbacknageen():
    webbrowser.open_new(r"https://www.facebook.com/Nageen9211")


def callbackshreyash():
    webbrowser.open_new(r"https://www.facebook.com/shreyash.iglesias")


def callbackaniket():
    webbrowser.open_new(r"https://www.facebook.com/profile.php?id=100011739582793")


def callsource():
    webbrowser.open_new(r"https://github.com/sumitdaroch/cardgame")


def deve():
    newwindow = Toplevel()
    newwindow.title("Contributors")
    newwindow.geometry("300x170")
    abutton = Button(newwindow, text="1. Sumit kumar Daroch", command=callbacksumit)
    abutton.pack(side="top", fill=BOTH, )
    abutton.configure(background="LightSkyBlue1")
    bbutton = Button(newwindow, text="2. Nitin Dogra", command=callbacknitin)
    bbutton.pack(fill=BOTH)
    bbutton.configure(background="LightSkyBlue1")
    cbutton = Button(newwindow, text="3. Nageen Chand", command=callbacknageen)
    cbutton.pack(fill=BOTH)
    cbutton.configure(background="LightSkyBlue1")
    dbutton = Button(newwindow, text="4. Shreyash Indurkar", command=callbackshreyash)
    dbutton.pack(fill=BOTH)
    dbutton.configure(background="LightSkyBlue1")
    ebutton = Button(newwindow, text="5. Aniket", command=callbackaniket)
    ebutton.pack(fill=BOTH)
    ebutton.configure(background="LightSkyBlue1")
    fbutton = Button(newwindow, text="Source Code", command=callsource)
    fbutton.pack(fill=BOTH)
    fbutton.configure(background="LightSkyBlue1")






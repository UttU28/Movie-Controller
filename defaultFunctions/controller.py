import pyautogui as py

def clickMainController():
    py.click()

def moveupMainController():
    x,y = py.position()
    py.moveTo(x,y-100)

def moveleftMainController():
    x,y = py.position()
    py.moveTo(x-100,y)

def movedownMainController():
    x,y = py.position()
    py.moveTo(x,y+100)

def moverightMainController():
    x,y = py.position()
    py.moveTo(x+100,y)

import pyautogui as py

def scrollUpMain():
    py.scroll(100)

def clickMain():
    py.click()

def moveUpMain():
    x,y = py.position()
    py.moveTo(x,y-20)

def closeTabMain():
    py.keyDown('ctrl')
    py.press('w')
    py.keyUp('ctrl')

def refreshMain():
    py.press('f5')

def scrollDownMain():
    py.scroll(-100)

def moveleftMain():
    x,y = py.position()
    py.moveTo(x-20,y)

def movedownMain():
    x,y = py.position()
    py.moveTo(x,y+20)

def moverightMain():
    x,y = py.position()
    py.moveTo(x+20,y)

def goBackMain():
    py.keyDown('alt')
    py.press('left')
    py.keyUp('alt')
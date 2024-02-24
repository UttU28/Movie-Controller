import pyautogui as py

def searchFMovies(searchData):
    py.click(1110, 110)
    py.keyDown('ctrl')
    py.press('a')
    py.keyUp('ctrl')
    py.press('backspace')
    py.typewrite(searchData)
    py.press('enter')

def newTabFM():
    py.keyDown('ctrl')
    py.press('t')
    py.keyUp('ctrl')
    py.typewrite('https://fmovies.app/')
    py.press('enter')

def click1FM():
    py.click(950, 665)

def volUpFM():
    py.press('up')

def goBackFM():
    pass

def startFM():
    py.press('0')

def click2FM():
    py.click(1320, 670)

def fullScreenFM():
    py.press('f')

def volDownFM():
    py.press('down')
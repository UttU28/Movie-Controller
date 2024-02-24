import pyautogui as py

def escape():
    py.keyDown('alt')
    py.press('tab')
    py.keyUp('alt')

def desktop():
    py.keyDown('win')
    py.press('d')
    py.keyUp('win')

def fullScreen():
    py.press('f')

def one():
    py.keyDown('ctrl')
    py.press('1')
    py.keyUp('ctrl')

def two():
    py.keyDown('ctrl')
    py.press('2')
    py.keyUp('ctrl')

def three():
    py.keyDown('ctrl')
    py.press('3')
    py.keyUp('ctrl')

def four():
    py.keyDown('ctrl')
    py.press('4')
    py.keyUp('ctrl')

def nextTab():
    py.keyDown('ctrl')
    py.press('tab')
    py.keyUp('ctrl')

def youTubeButton():
    pass

def googleChromeButton():
    pass

def fMoviesButton():
    pass

def netflixButton():
    pass

def primeVideosButton():
    pass
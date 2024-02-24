import pyautogui as py

def volumeIncrease():
    py.press('volumeup')
    py.press('volumeup')

def previousTrack():
    py.keyDown('alt')
    py.press('left')
    py.keyUp('alt')

def backSeek():
    py.press('left')

def pause():
    py.press('space')

def forwardSeek():
    py.press('right')

def nextTrack():
    py.keyDown('shift')
    py.press('n')
    py.keyUp('shift')

def volumeDecrease():
    py.press('volumedown')
    py.press('volumedown')

def escape():
    py.keyDown('alt')
    py.press('tab')
    py.keyUp('alt')

def scrollUp():
    py.scroll(1000)

def closeTab():
    py.keyDown('ctrl')
    py.press('w')
    py.keyUp('ctrl')

def desktop():
    py.keyDown('win')
    py.press('d')
    py.keyUp('win')

def click():
    py.click(1325, 555)

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

def five():
    py.keyDown('ctrl')
    py.press('5')
    py.keyUp('ctrl')

def six():
    py.keyDown('ctrl')
    py.press('6')
    py.keyUp('ctrl')

def seven():
    py.keyDown('ctrl')
    py.press('7')
    py.keyUp('ctrl')

def eight():
    py.keyDown('ctrl')
    py.press('8')
    py.keyUp('ctrl')

def refresh():
    py.press('f5')

def nextTab():
    py.keyDown('ctrl')
    py.press('tab')
    py.keyUp('ctrl')

def seachYouTube():
    pass

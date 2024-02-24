import pyautogui as py

def searchPrime(searchData):
    py.click(1710, 110)
    py.keyDown('ctrl')
    py.press('a')
    py.keyUp('ctrl')
    py.press('backspace')
    py.typewrite(searchData)
    py.press('enter')

def newTabAP():
    py.keyDown('ctrl')
    py.press('t')
    py.keyUp('ctrl')
    py.typewrite('https://www.primevideo.com/')
    py.press('enter')

def volUpAP():
    py.press('up')
    
def goBackAP():
    pass

def startAP():
    py.press('0')

def fullScreenAP():
    py.press('f')

def volDownAP():
    py.press('down')
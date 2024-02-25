import pyautogui as py

def searchFMovies(searchData):
    py.keyDown('ctrl')
    py.press('l')
    py.keyUp('ctrl')
    py.typewrite(f'https://fmoviesz.to/filter?keyword={"+".join(searchData.strip().split(" "))}')
    py.press('enter')
    # py.typewrite(searchData)

def newTabFM():
    py.keyDown('ctrl')
    py.press('t')
    py.keyUp('ctrl')
    py.typewrite('https://fmoviesz.to/home')
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
import pyautogui as py

def searchIBomma(searchData):
    py.keyDown('ctrl')
    py.press('l')
    py.keyUp('ctrl')
    py.typewrite(f'https://search-v2.ibomma.support/?label=telugu&q={"+".join(searchData.strip().split(" "))}')
    py.press('enter')
    # py.typewrite(searchData)

def newTabIB():
    py.keyDown('ctrl')
    py.press('t')
    py.keyUp('ctrl')
    py.typewrite('https://com.ibomma.lol/telugu-movies/')
    py.press('enter')

def click1IB():
    py.click(950, 665)

def volUpIB():
    py.press('up')

def goBackIB():
    pass

def startIB():
    py.press('0')

def click2IB():
    py.click(1320, 670)

def fullScreenIB():
    py.press('f')

def volDownIB():
    py.press('down')
'''
lib for pyautogui

'''

'''
imports

pip statements

pip install pyautogui
'''

import pyautogui

def get_screen():
    screenWidth, screenHeight = pyautogui.size()
    return screenWidth, screenHeight

def get_mouse():
    currentMouseX, currentMouseY = pyautogui.position()
    return currentMouseX, currentMouseY

def mouse_click():
    pyautogui.click()

def mouse_move(distanceX, distanceY, currentMouseX, currentMouseY, screenWidth, screenHeight):
    newMouseX = currentMouseX + distanceX
    newMouseY = currentMouseY + distanceY

    if newMouseX>screenWidth/2:
        newMouseX = screenWidth/2
    elif newMouseX>(screenWidth/2)-screenWidth:
        newMouseX = (screenWidth/2)-screenWidth

    if newMouseY>screenHeight/2:
        newMouseY = screenHeight/2
    elif newMouseY>(screenHeight/2)-screenHeight:
        newMouseY = (screenHeight/2)-screenHeight

def mouse_other_click(type, distance, currentMouseX, currentMouseY, screenWidth, screenHeight):
    pass

def keyboard_action():
    pass


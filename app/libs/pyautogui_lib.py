'''
lib for pyautogui

'''

'''
imports

pip statements

pip install pyautogui
'''

import pyautogui

'''
Defs
'''

#Get dimensions of the screen

def get_screen():
    screenWidth, screenHeight = pyautogui.size()
    return screenWidth, screenHeight

#Get mouse position

def get_mouse():
    currentMouseX, currentMouseY = pyautogui.position()
    return currentMouseX, currentMouseY

#Perform a mouse click

def mouse_click():
    pyautogui.click()

#Move the mouse

def mouse_move(distanceX, distanceY, currentMouseX, currentMouseY, screenWidth, screenHeight):
    
    #Get the coords the mouse should go to

    newMouseX = currentMouseX + distanceX
    newMouseY = currentMouseY + distanceY

    #Check if they exceed the limits of the screen

    if newMouseX>screenWidth/2:
        newMouseX = screenWidth/2
    elif newMouseX>(screenWidth/2)-screenWidth:
        newMouseX = (screenWidth/2)-screenWidth

    if newMouseY>screenHeight/2:
        newMouseY = screenHeight/2
    elif newMouseY>(screenHeight/2)-screenHeight:
        newMouseY = (screenHeight/2)-screenHeight

    #Move the mouse.

    pyautogui.moveTo(newMouseX, newMouseY)

#A few other mouse actions involving clicking

def mouse_other_click(type, distanceX=None, distanceY=None, currentMouseX=None, currentMouseY=None, screenWidth=None, screenHeight=None):

    #Double click

    if type=='double_click':

        pyautogui.doubleClick()

    #Click and drag

    if type=='click_and_drag':
        
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

        pyautogui.dragTo(newMouseX, newMouseY)   

#Perform different keyboard actions

def keyboard_action(action, input):

    #Press a key

    if action=='press_key':
        pyautogui.press(input)

    #Type text

    elif action=='type_text':
        pyautogui.typewrite(input)

    #Perform a keyboard shortcut

    elif action=='keyboard_shortcut':
        pyautogui.hotkey(input)
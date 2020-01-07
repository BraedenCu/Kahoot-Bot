import time
import random
import pyautogui
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
import pynput

keyboard = Controller()

print('type the pin plz')
pin = int(input())
pinreal = str(pin)
print('how many bots?')
numofbots = int(input())
print('randomname? 0 if no, 1 if yes')
randomname = int(input())

apple = 0
time.sleep(1)

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def onebot():
    
    randnumber = random.randint(1,5000)
    nickname = 'pp' + str(randnumber)
    #step one, move to plus tab 1349
    pyautogui.moveTo(1350, 40, duration=0.2)
    pyautogui.click(1350, 40)

    #move to search bar
    pyautogui.moveTo(559, 43, duration=0.2)
    pyautogui.click(449, 43)

    #type in search bar
    pyautogui.typewrite('kahoot.it')
    keyboard.press(Key.enter)

    #enter game pin
    pyautogui.moveTo(698, 418, duration=0.15)

    #click on pin number, type pin, and press enter
    pyautogui.click(698, 418)
    pyautogui.doubleClick(698, 418)
    pyautogui.typewrite(pinreal)
    keyboard.press(Key.enter)
    time.sleep(1)
    #pyautogui.moveTo(698, 500, duration=0.1)
    #pyautogui.click(698, 500)

    #type in nickname 418 prev
    pyautogui.click(698, 450)
    pyautogui.doubleClick(698, 450)
    pyautogui.typewrite(nickname)
    keyboard.press(Key.enter)
    
    time.sleep(1)

def onebotrandomname():

    randnumber = random.randint(1,5000)
    nickname = 'pp' + str(randnumber)
    #step one, move to plus tab 1349
    pyautogui.moveTo(1350, 40, duration=0.2)
    pyautogui.click(1350, 40)

    #move to search bar
    pyautogui.moveTo(559, 43, duration=0.2)
    pyautogui.click(449, 43)

    #type in search bar
    pyautogui.typewrite('kahoot.it')
    keyboard.press(Key.enter)

    #enter game pin
    pyautogui.moveTo(698, 418, duration=0.1)

    #click on pin number, type pin, and press enter
    pyautogui.click(698, 418)
    pyautogui.doubleClick(698, 418)
    pyautogui.typewrite(pinreal)
    keyboard.press(Key.enter)
    time.sleep(1)
    #pyautogui.moveTo(698, 500, duration=0.1)
    #pyautogui.click(698, 500)

    #type in nickname 418 prev
    pyautogui.click(698, 450)
    pyautogui.doubleClick(698, 450)
    pyautogui.typewrite(nickname)
    keyboard.press(Key.enter)
    #time.sleep(1)

    pyautogui.click(672, 586)
    pyautogui.doubleClick(672, 586)
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)
    keyboard.press(Key.enter)
    
    
while(1==1):

    if randomname == 0:
        onebot()
        print('one cycle done -_- xP')

    if randomname == 1:
        onebotrandomname()
        print('one cycle done -_- xD')
        
    apple = apple + 1

    if apple == numofbots:
        break

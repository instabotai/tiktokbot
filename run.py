import pyautogui
import time
import random
screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.


currentMouseX, currentMouseY = pyautogui.position() # Retursn two integes, the x and y of the mouse cursor's current position.

#pyautogui.moveTo(380, 290)

def get_around_ads(sleep):
        pyautogui.click(20, 140) # close left side
        time.sleep(sleep)
        pyautogui.click(20, 140) # close left side
        time.sleep(1)

def liker(sleep):
    time.sleep(1)
    pyautogui.click(380, 290)
#    pyautogui.click(40, 790)
    time.sleep(sleep)

def comment_liker(sleep):
        pyautogui.click(420, 450)
        time.sleep(1)
        pyautogui.click(410, 190)
        time.sleep(1)
        pyautogui.click(420, 120)
        time.sleep(1)
        get_around_ads(1)
        time.sleep(sleep)
        pyautogui.click(40, 790)
        time.sleep(1)

def comment(sleep):
        comment = ["this is cool", "yeaah", "hehe", "hehehe", ";)", ":)", "wow", "wooow", "nice", "cool", "awesome", "yes", "this is awesome", "agree"]
        pyautogui.click(420, 450)
        time.sleep(0.5)
        pyautogui.click(10, 330)
        time.sleep(0.5)
        comment = random.choice(comment)
        pyautogui.typewrite(comment)
        time.sleep(0.5)
        pyautogui.click(420, 790)
        time.sleep(0.5)
        pyautogui.click(420, 120) # close right side
        pyautogui.click(20, 140) # close left side
        time.sleep(0)
        pyautogui.click(20, 140) # close left side
        time.sleep(2)
        pyautogui.click(40, 790)
        time.sleep(1)
        pyautogui.click(40, 790)
        time.sleep(2)

while True:
    comment_liker(4)
    #comment(10)
    liker(5)

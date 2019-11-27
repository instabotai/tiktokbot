import pyautogui
import time
import random
screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.


currentMouseX, currentMouseY = pyautogui.position() # Retursn two integes, the x and y of the mouse cursor's current position.
class Bot():
    
    def __init__ (self, x=0):
        self.x = x
        self.home = pyautogui.locateOnScreen('img/home.png', confidence=0.9)

    def get_around_ads(self, sleep):
            pyautogui.click(35, 140) # close left side
            time.sleep(sleep)
            pyautogui.click(35, 140) # close left side
            time.sleep(0.7)
            pyautogui.click(35, 140) # close left side
            time.sleep(0.7)

    def liker(sleep):
        time.sleep(1)
        liker = pyautogui.locateOnScreen('img/heart.png', confidence=0.9)
        time.sleep(sleep)

    def comment_liker(self, sleep):
            pyautogui.click(95, 10) # go back to tiktok app
            time.sleep(0.6)
            pyautogui.click(420, 450)
            time.sleep(0.6)
            i = 0
            while i in range(2000):
                like = pyautogui.locateOnScreen('like.png', confidence=0.9)
                time.sleep(0.1)
                pyautogui.click(like)
                time.sleep(0)
                pyautogui.scroll(-3)
                time.sleep(0.4)
                self.x += 1
                print(str(self.x))
                i += 1
                if like == None:
                    break
            #like = pyautogui.locateOnScreen('like.png', confidence=0.9) 
            pyautogui.click(like)
            #pyautogui.click(410, 190)
            time.sleep(0.3)
            pyautogui.click(420, 120)
            time.sleep(0.4)
            self.get_around_ads(1)
            time.sleep(sleep)
            pyautogui.click(95, 10) # go back to tiktok app
            pyautogui.click(40, 790)
            time.sleep(0.3)

    def comment(self, sleep):
            comment = ["this is cool", "yeaah", "hehe", "hehehe", ";)", ":)", "wow", "wooow", "nice", "cool", "awesome", "yes", "this is awesome", "agree"]
            pyautogui.click(420, 450)
            time.sleep(1.5)
            pyautogui.click(10, 330)
            time.sleep(1.5)
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
            self.x += 1
            print(str(self.x))
            time.sleep(sleep)

    def follow_user(self, sleep):
        home = pyautogui.locateOnScreen('img/home.png', confidence=0.9)
        time.sleep(0.1)
        pyautogui.click(home)
        time.sleep(1)
        follow_buttom = pyautogui.locateOnScreen('img/follow.png', confidence=0.9)
        pyautogui.click(follow_buttom)
        time.sleep(sleep)
        self.x += 1
        print(str(self.x))

bot = Bot()
while True:
#    bot.comment_liker(1)
    bot.follow_user(45)
    #bot.comment(10)
    #comment(10)
    #liker(5)

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

    def liker(self, sleep):
        time.sleep(2)
        liker = pyautogui.locateOnScreen('img/heart.png', confidence=0.8)
        pyautogui.click(liker)
        time.sleep(sleep)
        self.x += 1
        print(str(self.x))

    def comment_liker(self, sleep):
            pyautogui.click(95, 10) # go back to tiktok app
            time.sleep(0.6)
            pyautogui.click(420, 450)
            time.sleep(0.6)
            i = 0
            while i in range(2000):
                like = pyautogui.locateOnScreen('img/like.png', confidence=0.9)
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

    def confirm(self):
        confirm = pyautogui.locateOnScreen('img/confirm.png', confidence=0.8)
        pyautogui.click(confirm)

    def comment(self, sleep):
            comment = ["this is cool", "yeaah", "hehe", "hehehe", ";)", ":)", "wow", "wooow", "nice", "cool", "awesome", "yes", "this is awesome", "agree"]
            time.sleep(2)
            comments = pyautogui.locateOnScreen('img/comment.png', confidence=0.8)
            print("does comment box exist", comments)
            time.sleep(1)
            pyautogui.click(comments)
            time.sleep(1)
            comment = random.choice(comment)
            time.sleep(1)
            add_comment = pyautogui.locateOnScreen('img/add_comment.png', confidence=0.9)
            time.sleep(1)
            pyautogui.click(add_comment)
            time.sleep(1)
            pyautogui.typewrite(comment)
            time.sleep(1)
            click = pyautogui.locateOnScreen('img/commentclick.png', confidence=0.9)
            time.sleep(1)
            pyautogui.click(click)
            time.sleep(2)
            close = pyautogui.locateOnScreen('img/close.png', confidence=0.8)
            time.sleep(2)
            pyautogui.click(close)
            time.sleep(1)
   #         self.confirm()
            time.sleep(sleep)
            self.x += 1
            print(str(self.x))

    def go_back_page(self):
        go_back = pyautogui.locateOnScreen('img/back.png', confidence=0.9)
        pyautogui.click(go_back)


    def follow_user(self, sleep):
        time.sleep(1)
        follow_buttom = pyautogui.locateOnScreen('img/follow.png', confidence=0.8)
        print("does follow buttom exist", follow_buttom)
        pyautogui.click(follow_buttom)
        time.sleep(1)
        self.go_back_page()
        time.sleep(sleep)


bot = Bot()
while True:
    home = pyautogui.locateOnScreen('img/home.png', confidence=0.8)
    print(home)
    time.sleep(2)
    pyautogui.click(home)
    time.sleep(4)
    #bot.comment_liker(5)
    bot.follow_user(65 + random.random())
    time.sleep(10)
    #bot.comment(10)
    bot.comment(4)
    time.sleep(3)
   # bot.liker(1 + random.random())

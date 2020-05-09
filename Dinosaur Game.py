import pyautogui 
from PIL import Image, ImageGrab 
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(460, 490):
        for j in range(150, 190):
            if data[i, j] < 100:
                hit("down")
                return
    # Draw the rectangle for cactus
    for i in range(470, 510):
        for j in range(190, 230):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
    '''
        # Draw the rectangle for cactus
        for i in range(470, 510):
            for j in range(190, 230):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(460, 490):
            for j in range(150, 190):
                data[i, j] = 171

        image.show()
        break
    '''

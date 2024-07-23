"""
This little program automatically moves your mouse across the screen to
random points on the screen
"""
import pyautogui
import random
import time

while True:
    # Move the mouse to a random location
    x, y = pyautogui.size()
    pyautogui.moveTo(x * random.uniform(0, 1), y * random.uniform(0, 1))
    time.sleep(15)

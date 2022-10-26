from operator import invert
import pyautogui 
import time


pyautogui.hotkey("win", "r")

time.sleep(2)

pyautogui.write('MicrosoftEdge "https://www.youtube.com/watch?v=dQw4w9WgXcQ"',interval=0.1)

time.sleep(2)

pyautogui.press("enter")
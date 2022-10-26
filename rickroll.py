from operator import invert
import pyautogui 
import time

#Abre el Ejecturar
pyautogui.hotkey("win", "r")

#Espera 2 segundos
time.sleep(2)

#Comienza a escribir el navegador y la pagina a la que quiera ir
pyautogui.write('MicrosoftEdge "https://www.youtube.com/watch?v=dQw4w9WgXcQ"',interval=0.1)

#Espera 2 segundos y oprime enter
time.sleep(2)

pyautogui.press("enter")
import pyautogui
import time

while True:
    location = pyautogui.locateCenterOnScreen('Cryinoah/google.PNG')
    if location is not None:
        pyautogui.click(location[0], location[1])
        pyautogui.typewrite('Minho panty dirty')
        pyautogui.press('enter', presses = 5)
        time.sleep(0.5)

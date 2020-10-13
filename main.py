import time
import pyautogui

loop = 0

while loop < 10000:
    try:
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen("source/01.png"))
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen("source/02.png"))
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen("source/03.png"))
        time.sleep(62)
        pyautogui.click(pyautogui.locateCenterOnScreen("source/04.png"))
        loop += 1
    except:
        break
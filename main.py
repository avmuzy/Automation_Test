import pyautogui
import time
#alert message
pyautogui.alert("Vamos abrir o Chrome!")
pyautogui.PAUSE = 0.5

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://mail.google.com/')


import pyautogui
import time
pyautogui.alert('Eh hora de Rock')
pyautogui.PAUSE = 0.5
pyautogui.press('startp')
time.sleep(1)
pyautogui.write('Spotify app')
pyautogui.press('enter')

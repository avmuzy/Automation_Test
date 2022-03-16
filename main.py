import pyautogui
import time
#alert message
pyautogui.alert("Vamos dar bom dia!")
pyautogui.PAUSE = 0.5

pyautogui.press('winleft')
pyautogui.write('Firefox')
pyautogui.press('enter')
time.sleep(10)
pyautogui.write('https://discord.com/channels/821791958744957028/902631152886636574')
time.sleep(5)
pyautogui.press('enter')


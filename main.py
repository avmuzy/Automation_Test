import pyautogui
import time
#alert message
pyautogui.alert("Vamos dar bom dia!")
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('Firefox')
pyautogui.press('enter')
time.sleep(20)
pyautogui.write('https://discord.com/channels/821791958744957028/938486939382874172')
time.sleep(5)
pyautogui.press('enter')
time.sleep(15)
pyautogui.write('Boa noite grupo 12. ')
pyautogui.write(' Essa mensagem foi escrita usando pyautogui')
pyautogui.press('enter')





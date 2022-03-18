from tkinter import *
import pyautogui
import time
root=Tk()
root.geometry('200x200')
message = Label(root, text='Vamos dar Bom DIA!')
message.pack()
myframe = Frame(root)
myframe.pack()


pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('Firefox')
pyautogui.press('enter')
time.sleep(20)
pyautogui.write('https://discord.com/channels/821791958744957028/938486939382874172')
time.sleep(5)
pyautogui.press('enter')
time.sleep(15)
pyautogui.write('Boa dia grupo 12. ')
pyautogui.write(' Essa mensagem foi escrita usando pyautogui')
pyautogui.press('enter')
root.mainloop()




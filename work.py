from tkinter import *

root = Tk()
root.geometry('200x200')
message = Label(root, text='Time to work!')
message.pack()
myframe = Frame(root)
myframe.pack()


# defining the button function

def run():
    import pyautogui
    import time
    pyautogui.press('winleft')
    pyautogui.write('Firefox')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.write('https://discord.com/channels/821791958744957028/938486939382874172')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.press('winleft')
    pyautogui.write('Pycharm')
    pyautogui.press('enter')

button1 = Button(myframe, text="Run", command=run, width=15)
button1.pack(pady=5)
root.mainloop()


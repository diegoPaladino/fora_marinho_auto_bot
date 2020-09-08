#foramarinho_auto_bot

import pyautogui as p
import time as t
import schedule as s
import winsound as w

p.moveTo(1085,-249)  #<<<<<<<<<<<<<<<<<<<<<<<<<<< point of chat
p.click()
t.sleep(0.3)

def job():
    p.write('#FORAMARINHO')
    t.sleep(4)
    p.hotkey('enter')
    w.Beep(frequency=2500,duration=1000)

s.every().minute.do(job)

while True:
    s.run_pending()
    t.sleep(1)
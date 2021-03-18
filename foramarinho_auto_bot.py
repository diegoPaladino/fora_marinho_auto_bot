#foramarinho_auto_bot

import pyautogui as p
import time as t
import schedule as s
import winsound as w
from datetime import datetime

p.moveTo(x=1216, y=-240)  #<<<<<<<<<<<<<<<<<<<<<<<<<<< point of chat
p.click()
t.sleep(0.3)

def job():
    p.write('#FORAMARINHO')
    t.sleep(4)
    p.hotkey('enter')
    w.Beep(frequency=2500,duration=1000)
    print (datetime.now())

s.every().minute.do(job)
#
while True:
    s.run_pending()
    t.sleep(1)
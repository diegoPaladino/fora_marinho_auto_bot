#foramarinho_auto_bot

import pyautogui as p
import time as t
import schedule as s
import winsound as w
from datetime import datetime

texto = "#ForaMarinho #ForaCandil"

p.moveTo(x=1136, y=-276)  #<<<<<<<<<<<<<<<<<<<<<<<<<<< point of chat
p.click()
t.sleep(0.3)

p.write(texto)
t.sleep(4)
p.hotkey('enter')
w.Beep(frequency=2500,duration=1000)
print (datetime.now())

def job():
    p.write(texto)
            
            
    t.sleep(4)
    p.hotkey('enter')
    w.Beep(frequency=2500,duration=1000)
    print (datetime.now())

s.every().minute.do(job)
#
while True:
    s.run_pending()
    t.sleep(1)
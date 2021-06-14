#foramarinho_auto_bot

import pyautogui as p
import time as t
import schedule as s
import winsound as w
from datetime import datetime

p.moveTo(x=1216, y=-240)  #<<<<<<<<<<<<<<<<<<<<<<<<<<< point of chat
p.click()
t.sleep(0.3)

p.write('MANAUARA - Fefito do Amazonas/Norte. HUUUUM VAAAI CARNEIRIIIIIIIIIIIINHO!!! #ForaMarinho')
t.sleep(4)
p.hotkey('enter')
w.Beep(frequency=2500,duration=1000)
print (datetime.now())

def job():
    p.write('MANAUARA - Fefito do Amazonas/Norte. HUUUUM VAAAI CARNEIRIIIIIIIIIIIINHO!!! #ForaMarinho')MANAUARA - Fefito do Amazonas/Norte. HUUUUM VAAAI CARNEIRIIIIIIIIIIIINHO!!! #ForaMarinho
            
            
    t.sleep(4)
    p.hotkey('enter')
    w.Beep(frequency=2500,duration=1000)
    print (datetime.now())

s.every().minute.do(job)
#
while True:
    s.run_pending()
    t.sleep(1)
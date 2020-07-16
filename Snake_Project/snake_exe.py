import pyautogui as pg
import time

def game_exe():
    pg.hotkey('command', 'space') 
    pg.write('Terminal')
    pg.hotkey('enter')
    time.sleep(1) # have to wait this amount of time before executing futher
    pg.typewrite('cd Desktop')
    pg.hotkey('enter')
    pg.typewrite('cd Snake_Project')
    pg.hotkey('enter')
    pg.typewrite('pzthon3 snake.pz') # has to change the typed filename because of the different keyboard outside of US
    pg.hotkey('enter')

game_exe()

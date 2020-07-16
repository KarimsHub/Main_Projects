# Note: this file is acutally only created to automate the execution of the file on my computer. It´s not neccessary to use any of this code to run the game itself

import pyautogui as pg
import time

def game_exe():
    pg.hotkey('command', 'space') 
    pg.write('Terminal')
    pg.hotkey('enter')
    time.sleep(1) # have to wait this amount of time before executing futher
    pg.typewrite('cd Desktop')
    pg.hotkey('enter')
    pg.typewrite('cd Falling_Project')
    pg.hotkey('enter')
    pg.typewrite('pzthon3 Falling.pz') # has to change the typed filename because of the different keyboard outside of US
    pg.hotkey('enter')

game_exe()

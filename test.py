#!/usr/bin/python3
import random
import pyautogui as pg
import time

insulto = ('a dick', 'a bitch', 'stupid', 'black')


input("Press Enter when ready...")

time.sleep(8)
for i in range(11):
    a = random.choice(insulto)
    pg.displayMousePosition()
    pg.write('youre ' + a)
    pg.press('enter')
    time.sleep(0.1)

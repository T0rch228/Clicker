import pyautogui as pg
import time

pg.alert("Welcome to clicker. Plese choos the point")
time.sleep(2)
point = pg.position()
pg.alert(point)
x = 0
while x == 0:
    pg.click(point)

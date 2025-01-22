import pyautogui as pg
import time

pg.alert("Welcome to clicker. Plese choos the point")
time.sleep(2)
point = pg.position()
pg.alert(point)

while True:
    pg.click(point)
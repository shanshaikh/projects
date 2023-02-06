import pyautogui as py
import time

def draw_square(var = 10):
    iterator = int(var)
    py.moveTo(500, 500)
    py.click()
    for i in range(0, iterator):
        offset = 5
        py.moveRel(offset, offset)
        py.drag(50, 0, duration=0.5)
        py.drag(0, 50, duration=0.5)
        py.drag(-50, 0, duration=0.5)
        py.drag(0, -50, duration=0.5)
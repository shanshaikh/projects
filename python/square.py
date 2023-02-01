import pyautogui as py
import time
from multiprocessing import Process

pause = False
pause_key = '9'

def draw_square(var = 3):
    iterator = int(var)
    py.moveTo(500, 500)
    py.click()
    for i in range(0, iterator):
        if (pause):
            time.sleep(3)
            print('pause')
            iterator -= 1
            continue
        offset = 5
        py.moveRel(offset, offset)
        py.drag(50, 0, duration=0.5)
        py.drag(0, 50, duration=0.5)
        py.drag(-50, 0, duration=0.5)
        py.drag(0, -50, duration=0.5)
    print('done')

def query():
    while(1):
        print('test')
        time.sleep(1)
        val = input()
        print(str(val))
        if (pause_key in val):
            pause = True

##def test():
if __name__=='__main__':
    p1 = Process(target = query)
    p1.start()
    p2 = Process(target = draw_square)
    p2.start()

import _thread
import time


def get_num(name):
    num = 0
    while num < 5:
        time.sleep(1)
        num += 1
        print(num, name)


try:
    _thread.start_new_thread(get_num, ("T-1", ))
    _thread.start_new_thread(get_num, ("T-2", ))
except Exception as e:
    print(e)
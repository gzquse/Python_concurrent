import threading
import time

num = 0
lock = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if lock.acquire(1):
            num += 1
            msg = self.name + 'set num to' + str(num)
            print(msg)
            lock.release()


def add_num():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    add_num()
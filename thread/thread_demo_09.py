import threading
import time

con = threading.Condition()

num = 0

# producer


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        con.acquire()
        global num
        while True:
            print('adding fruits')
            num += 1
            print('nums', num)
            time.sleep(1)
            if num >= 5:
                print('enough')
                con.notify()
                con.wait()
        con.release()


class Consumer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self) -> None:
        con.acquire()
        global num
        while True:
            num -= 1
            time.sleep(1)
            if num <= 0:
                con.notify()
                con.wait()
        con.release()


if __name__ == '__main__':
    p = Producer()
    c = Consumer()
    p.start()
    c.start()
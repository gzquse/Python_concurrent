import threading
import time


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('start', self.name)
        print_time(self.name, self.counter, 2)
        print('end', self.name)


def print_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print(name, time.time())
        counter -= 1


t1 = MyThread(1, "T-1", 1)
t2 = MyThread(2, "T-2", 2)

t1.start()
t2.start()
t1.join()
t2.join()



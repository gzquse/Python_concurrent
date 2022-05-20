import time

from greenlet import greenlet


def task_1():
    while True:
        print('task 1 start')
        t2.switch()
        time.sleep(0.5)


def task_2():
    while True:
        print('task 2 start')
        t1.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    t1 = greenlet(task_1)
    t2 = greenlet(task_2)
    print(t1, t2)
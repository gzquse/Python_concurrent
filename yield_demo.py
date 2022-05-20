import time


def task1():
    while True:
        print("Task 1 start")
        yield
        print("Task 1 end")
        time.sleep(0.5)


def task2():
    while True:
        print("Task 2 start")
        yield
        print("Task 2 end")
        time.sleep(0.5)


if __name__ == '__main__':
    t1 = task1()
    t2 = task2()

    while True:
        next(t1)
        print('main thread')
        next(t2)
        
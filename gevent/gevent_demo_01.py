import gevent


def task_1(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)


if __name__ == '__main__':
    t1 = gevent.spawn(task_1, 5)
    t2 = gevent.spawn(task_1, 5)
    t3 = gevent.spawn(task_1, 5)

    t1.join()
    t2.join()
    t3.join()
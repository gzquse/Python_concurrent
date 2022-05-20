import os
import time
from multiprocessing import Process


def worker():
    print('子进程运行, pid: {0}, ppid: {1}'.format(os.getpid(), os.getppid()))
    time.sleep(1)
    print('子进程结束, pid:{0}'.format(os.getpid()))


def main():
    print('主进程，pid={0}'.format(os.getpid()))
    p = [Process(target=worker(), args=(), name='worker' + str(i)) for i in range(2)]
    for i in range(2):
        p[i].start()
    for i in range(2):
        p[i].join()
    print('主进程结束, pid:{0}'.format(os.getpid()))


if __name__ == '__main__':
    main()
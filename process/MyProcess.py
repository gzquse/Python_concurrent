import time
from multiprocessing import Process
import os


class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        print('子进程运行, pid: {0}, ppid: {1}'.format(os.getpid(),os.getppid()))
        time.sleep(1)
        print('子进程结束, pid:{0}'.format(os.getpid()))


def main():
    print('主进程开始, pid={0}'.format(os.getpid()))
    my = MyProcess()
    my.start()
    print('主进程开始, pid={0}'.format(os.getpid()))


if __name__ == '__main__':
    main()
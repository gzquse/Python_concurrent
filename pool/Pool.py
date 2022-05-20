import os
import time
from multiprocessing import Pool


def worker(count):
    print('子进程运行, pid: {0}, ppid: {1}, 编号: {2}'.format(os.getpid(), os.getppid(), count))
    time.sleep(1)
    print('子进程结束, pid:{0}, ppid: {1}, 编号:{2}'.format(os.getpid(), os.getppid(), count))


def main():
    print('主进程开始, pid: {0}'.format(os.getpid()))
    p_list = Pool(5)
    for i in range(10):
        # p_list.apply(worker, args=(i,))
        p_list.apply_async(worker, args=(i,))
    p_list.close()
    p_list.join()
    print('子进程结束, pid:{0}'.format(os.getpid()))


if __name__ == '__main__':
    main()

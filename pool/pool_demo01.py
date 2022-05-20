import time
from threading import Thread, current_thread
from queue import Queue


class WorkManager(object):

    def __init__(self, max_threads=2):
        self.max_threads = max_threads
        self.task_queue = Queue()
        self.thread_pool = []

    def appy_async(self, task, *args):
        self.task_queue.put((task, args))

    def close(self):
        if self.task_queue.qsize() < self.max_threads:
            self.max_threads = self.task_queue.qsize()
        for _ in range(self.max_threads):
            self.thread_pool.append(Work(self.task_queue))

    def wait_all_complete(self):
        for t in self.thread_pool:
            if t.isAlive():
                t.join()


class Work(Thread):
    def __init__(self, q):
        super(Work, self).__init__()
        self.q = q
        self.start()

    def run(self) -> None:
        while True:
            try:
                task, args = self.q.get(block=False)
                task(*args)
                self.q.task_done()
            except:
                break


def do_task(*args):
    print(current_thread().name, '--start--')
    time.sleep(0.5)
    print(current_thread().name, '--end')


if __name__ == '__main__':
    pool_manager = WorkManager(10)
    for i in range(100):
        pool_manager.appy_async(do_task, i)
    pool_manager.close()
    pool_manager.wait_all_complete()
    print('done')
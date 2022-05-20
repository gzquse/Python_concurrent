import time
from threading import Thread, Lock, current_thread, Condition
from queue import Queue


class ConcurrentQueue():
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.condition = Condition(Lock())
        self.q = Queue()

    def get(self):
        with self.condition:
            while self.q.empty():
                print('sale', current_thread().name, 'empty')
                self.condition.wait(timeout=30)

            obj = self.q.get()
            self.condition.notify()  # notify produce
        return obj

    def put(self, obj):
        with self.condition:
            while self.q.qsize() >= self.max_size:
                print('producer', current_thread().name, 'full wait to sell')

            self.q.put(obj)
            self.condition.notify()  # notify saleman


def producer(q, start, end):
    for i in range(start, end):
        obj = 'gold %d' % i
        print('producer', current_thread().name, obj)
        q.put(obj)
        time.sleep(0.2)


def consumer(q):
    for i in range(500):
        obj = q.get()
        print('consumer', current_thread().name, obj)
        time.sleep(0.2)


def start_thread(threads):
    for i in threads:
        i.start()


def wait_all(threads):
    for i in threads:
        i.join()


if __name__ == '__main__':
    q = ConcurrentQueue(29)
    seq = ((1000, 2000), (3000, 4000), (5000, 6000))

    ps = [Thread(target=producer, args=(q, *seq[_])) for _ in range(3)]
    cs = [Thread(target=consumer, args=(q,)) for _ in range(5)]

    start_thread(ps + cs)
    wait_all(ps + cs)

    print('Done')

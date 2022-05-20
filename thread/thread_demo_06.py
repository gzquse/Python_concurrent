import queue
import threading
import time

flag = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print("start"+ self.name)
        process_data(self.name, self.q)
        print("end"+self.name)


def process_data(name, q):
    while not flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data=q.get()
            queue_lock.release()
            print('name'+'processing'+data)
        else:
            queue_lock.release()
        time.sleep(1)


thread_list = ['Thread_1', 'Thread-2', "Thread_3"]
process_list = ['one', 'two', 'three', 'four', 'five']
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
t_id = 1


for name in thread_list:
    thread = MyThread(t_id, name, work_queue)
    thread.start()
    threads.append(thread)
    t_id += 1


# into queue
queue_lock.acquire()
for item in process_list:
    work_queue.put(item)
queue_lock.release()


# wait consume
while not work_queue.empty():
    pass


# ending
flag = 1
for t in threads:
    t.join()
print('main thread ending')

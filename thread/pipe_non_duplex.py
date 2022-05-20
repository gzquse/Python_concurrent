import time
from multiprocessing import Process, Pipe


def worker(conn):
    while True:
        msg = conn.recv()
        if msg == 'Done':
            break
        print('接受到的消息')


def main():
    conn1, conn2 = Pipe(duplex=False)
    p = Process(target=worker, args=(conn1,))
    p.start()

    for i in range(3):
        conn2.send(i)
        time.sleep(2)
    conn2.send('Done')
    p.join()
    print('结束')


if __name__ == '__main__':
    main()

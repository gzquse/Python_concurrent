import random
from multiprocessing import Pipe
from multiprocessing.context import Process


def client(conn):
    while True:
        msg = conn.recv()
        if msg == 'bye' or msg == 'Bye':
            break
        print('客户端接受消息', msg)
        conn.send(random.uniform(1, 3))
    print('客户端下线')


def server(conn):
    for i in range(10):
        conn.send('第%d个:hi' % i)
        msg = conn.recv()
        print('客户端发来的消息', msg)
    conn.send('Bye')


def main():
    conn1, conn2 = Pipe()
    p_client = Process(target=client, args=(conn1, ))
    p_client.start()

    p_server = Process(target=server, args=(conn2, ))
    p_server.start()

    p_server.join()
    p_client.join()
    print("结束")

if __name__ == '__main__':
    main()
import time
from threading import Lock, current_thread, Thread


def add_money(money):
    global my_money
    c_t = current_thread()
    with lock:
        print(c_t.name, 'balance:', my_money, 'deposit', money)
        my_money += money
        time.sleep(0.5)
        print(c_t.name, 'balance', my_money)


def get_money(money):
    global my_money
    c_t = current_thread()
    with lock:
        print(c_t.name, 'balance:', my_money, 'deposit', money)
        my_money -= money
        time.sleep(0.5)
        print(c_t.name, 'balance', my_money)


if __name__ == '__main__':
    m_t = current_thread()
    print(m_t.name, 'system logging')
    my_money = 100000000
    lock = Lock()

    add_t = Thread(target=add_money, args=(200000, ))
    get_t = Thread(target=get_money, args=(100, ))
    add_t.start()
    get_t.start()

    add_t.join()
    get_t.join()

    print(m_t.name, 'balance', my_money)
from threading import Thread, current_thread, Lock, local

def t1():
    var.v = 1234
    print(current_thread().name, "local:", var.v)


if __name__ == '__main__':
    var = local()

    var.v = 456

    t = Thread(target=t1)
    t.start()
    t.join()

    print(current_thread().name, "local:", var.v)
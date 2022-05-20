import os
from threading import Thread, current_thread


def list_file(path):
    print(current_thread().name, 'finding %s file' % path)
    if os.path.exists(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isdir(file_path):
                list_file(file_path)
            else:
                print(file_path)


if __name__ == '__main__':
    t = Thread(target=list_file, args=(r'C:\Users\MartinLovesFey\PycharmProjects\concurrent_demo', ))
    t.start()
    t.join()
    print('end')
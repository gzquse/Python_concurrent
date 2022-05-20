import time

from gevent import monkey
import gevent
import requests


# def run():

# def t1(name):
#     for i in range(5):
#         print(name, i)
#         time.sleep(1)
#
#
# def t2(name):
#     for i in range(5):
#         print(name, i)
#         time.sleep(1)


if __name__ == '__main__':
    # monkey.patch_all()
    urls = [
        'https://www.google.com',
        'https://www.python.org'
    ]
    jobs = [gevent.spawn(lambda x: requests.get(x), url) for url in urls]
    gevent.joinall(
        jobs,
        timeout=0.5
        # [gevent.spawn(run, 'Task-1'),]
    )
    print('main thread')

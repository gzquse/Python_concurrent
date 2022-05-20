def customer():
    print('start customer')
    response = None
    while True:
        print('interrupt save')
        n = yield response
        print('get context')
        if not n:
            return
        print('customer consume %d' % n)
        response = 'ok'


def producer(c):
    print('start producer')
    c.send(None)
    print('continue')
    n = 0
    while n < 5:
        n += 1
        print('start produce already get %d goods'% n)
        print('this is %d time to yield' % (n+1))
        r = c.send(n) # yield

    c.close()


if __name__ == '__main__':
    c = customer()
    producer(c)
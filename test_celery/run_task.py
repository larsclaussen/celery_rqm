from tasks import test

if __name__ == '__main__':
    r = test.delay(1, 2, 3)
    print 'Task result:',r.result
import threading
'''
当线程次数多的时候，就出问题了，如何解决这个问题？
抢  锁住  解锁  出来
解决方式是以牺牲线程的性能为前提的
'''
count = 100

#创建锁
lock = threading.Lock()

def demo(num):
    global count
    for x in range(1,100000):
        lock.acquire()
        count += num
        count -= num
        lock.release()
    print('%s 线程结束之后count的值为%s'% (threading.current_thread().name,count))

def main():
    t1 = threading.Thread(target=demo,args=(3,))
    t2 = threading.Thread(target=demo,args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程读取count的值为%s'% count)
    print('主线程-子进程全部结束')

if __name__ == '__main__':
    main()
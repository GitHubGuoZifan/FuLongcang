import threading
import time

def demo(name):
    count = 200
    if name == 'change':
        #修改count的值
        count += 50
        print('t1读取的count的值为%s'% count)
    else:
        time.sleep(3)
        #读取count的值
        print('t2读取的count的值为%s'% count)

def main():
    t1 = threading.Thread(target=demo,args=('change',))
    t2 = threading.Thread(target=demo,args=('read',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程-子线程全部结束')

if __name__ == '__main__':
    main()
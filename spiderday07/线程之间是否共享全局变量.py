import threading
import time
name='林青霞'

def read():
    time.sleep(3)
    print('读取的name值为%s'% name)

def change():
    #修改全局变量
    global name
    name = '朱茵'
    print('修改后的name值为%s'% name)

def main():
    t1 = threading.Thread(target=read)
    t2 = threading.Thread(target=change)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主进程-子进程全部结束')

if __name__ == '__main__':
    main()
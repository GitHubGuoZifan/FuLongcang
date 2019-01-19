from multiprocessing import Process
import time
name = '林青霞'

def read():
    time.sleep(3)
    print('读取的name的值为%s'% name)

def change():
    #修改全局变量
    global name
    name = '朱茵'
    print('修改后的name值为%s'% name)

def main():
    p1 = Process(target=read)
    p2 = Process(target=change)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('主进程子进程全部结束')

if __name__ == '__main__':
    main()
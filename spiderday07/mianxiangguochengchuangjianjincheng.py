from multiprocessing import Process
import time
import os

def sing(name):
    print('唱歌进程传递进来的参数为%s'% name)
    print('唱歌进程的进程id号为%s'% os.getpid())
    print('唱歌进程的父进程id为%s'% os.getppid())
    for x in range(1,6):
        print('我在唱歌')
        time.sleep(1)
    print('唱歌进程结束')

def dance():
    print('跳舞的进程id为%s' % os.getpid())
    print('跳舞的父进程id为%s' % os.getppid())
    for x in range(1,6):
        print('我在跳舞')
        time.sleep(1)
    print('跳舞进程结束')

def main():
    name = '高圆圆'
    print('主进程的进程id为%s'% os.getpid())
    #创建子进程
    #主进程可以给子进程传递参数
    p_sing = Process(target=sing,args=(name,))
    p_dance = Process(target=dance)
    #启动进程
    p_sing.start()
    p_dance.start()

    #主进程需要等待子进程结束之后再执行
    p_sing.join()
    p_dance.join()
    print('主进程结束')

if __name__ == '__main__':
    main()
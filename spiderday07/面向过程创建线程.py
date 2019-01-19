import threading
import time

def sing(name):
    print('主线程传递过来的参数为%s'% name)
    print('sing线程的名字为%s'% threading.current_thread().name)
    for x in range(1,6):
        print('你喜欢唱女儿情')
        time.sleep(1)

def dance():
    print('dance线程的名字为%s'% threading.current_thread().name)
    for x in range(1,6):
        print('你喜欢跳钢管舞')
        time.sleep(1)

def main():
    #主线程  MainThread
    print('主线程的名字为%s'% threading.current_thread().name)
    name = '贾玲'
    #创建子线程
    t_sing = threading.Thread(target=sing,name='唱歌',args=(name,))
    t_dance = threading.Thread(target=dance)

    #启动线程
    t_sing.start()
    t_dance.start()

    #主线程等待子线程结束之后再结束
    t_sing.join()
    t_dance.join()

    print('主线程-子线程全部运行结束')

if __name__ == '__main__':
    main()

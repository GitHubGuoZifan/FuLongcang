import threading
import time
class SingThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.username = name
        self.name = '唱歌'

    def run(self):
        print('主线程过来的参数为%s' % self.username)
        for x in range(1,6):
            print('你喜欢女儿情')
            time.sleep(1)
class DanceThread(threading.Thread):
    def run(self):
        for x in range(1,6):
            print('你喜欢跳钢管舞')
            time.sleep(1)
def main():
    name = '柳岩'
    t_sing = SingThread(name)
    t_dance = DanceThread()

    t_sing.start()
    t_dance.start()

    t_sing.join()
    t_dance.join()
    print('主线程-子线程全部运行结束')

if __name__ == '__main__':
    main()
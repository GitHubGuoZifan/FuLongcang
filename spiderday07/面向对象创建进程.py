# threading.current_thread().name
#获取当前线程的名字
from multiprocessing import Process
import time
#写一个类，继承自Process类
class SingProcess(Process):

    #重写run方法，进程启动之后执行这个函数,重写这个函数名只能叫run,不能叫其他的
    def run(self):
        for x in range(1,6):
            print('我在唱最炫民族风')
            time.sleep(2)

class DanceProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print('主进程传递过来的参数为%s'% self.name)
        for x in range(1,6):
            print('我在跳广场舞')
            time.sleep(1)

def main():
    name='迪丽热巴'
    #创建子进程
    p_sing = SingProcess()
    p_dance = DanceProcess(name)

    p_sing.start()
    p_dance.start()

    p_sing.join()
    p_dance.join()
    print('主进程-子进程运行结束')

if __name__ == '__main__':
    main()
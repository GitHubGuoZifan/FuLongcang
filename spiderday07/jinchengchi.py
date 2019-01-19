from multiprocessing import Pool
import os
import time

def demo(name):
    print('当前的任务名字为--%s--,当前的进程id号为--%d--' % (name,os.getpid()))
    time.sleep(3)

def main():
    #创建一个进程池，进程池里面最多创建3个进程
    pol = Pool(3)
    lt = ['关云长','张翼德','赵子龙','马孟起','黄汉升','典韦','徐公明','夏元让'
          ,'许仲康','张文远']
    for name in lt:
        #给进程池添加任务
        pol.apply_async(demo,args=(name,))
    #关闭进程池，不能向里面添加数据了
    pol.close()
    #让主进程等待进程池中所有进程结束再结束
    pol.join()
    print('主进程-子进程全部结束')


if __name__ == '__main__':
    main()
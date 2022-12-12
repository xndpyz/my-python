import threading
import time
from queue import Queue

"""
线程间通信
1. 用全局变量+互斥锁
2. queue

线程同步：
Lock, RLock, Semaphores, Condition
concurrent 线程池

获取状态

join()
start()

feture 未来对象,任务容器
"""


class A(threading.Thread):
    def __init__(self, name, queue):
        super(A, self).__init__()
        self.name = name
        self.queue = queue

    def run(self) -> None:
        # time.sleep(2)
        for i in range(10):
            print(f"A set data...{i}")
            self.queue.put(i)
            # time.sleep(2)


class B(threading.Thread):
    def __init__(self, name, queue):
        super(B, self).__init__()
        self.name = name
        self.queue = queue

    def run(self) -> None:

        for i in range(10):
            val = self.queue.get()
            print(f"B get start...{val}")
            # time.sleep(2)


if __name__ == '__main__':
    queue = Queue()
    a = A("Producer a", queue)
    b = B("demo b", queue)

    a.start()
    b.start()
    a.join()
    b.join()

    print("end...")

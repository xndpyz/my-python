from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor



def fn(n):
    if n <= 2:
        return 1
    return fn(n - 1) + fn(n - 2)


if __name__ == '__main__':
    # windows 下的bug, linux/uinx 不需要 __name__ == '__main__'
    # 对于消耗cpu 的操作, 多进程要优于多线程
    # io 多的话, 多线程比较合适, 进程的切换浪费资源
    # concurrent.futures 未来对象

    """
    对于消耗CPU 的操作，  多进程要优于多线程
    io 多的话 多线程比较合适， 因为进程之间的切换浪费资源
    
    """
    with ProcessPoolExecutor(3) as executor:
        tasks = [executor.submit(fn, i) for i in range(20, 30)]
        # as_completed yield协程, 会先释放掉完成的任务
        for i in as_completed(tasks):
            print(i.result())



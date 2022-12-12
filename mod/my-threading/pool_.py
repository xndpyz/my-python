"""
线程池：
可以获取某一个线程的状态或者返回值
一个线程完成时，可以通知我们主线程
futures 可以让多进程和多线程编码接口一致

"""

from concurrent.futures import ThreadPoolExecutor, as_completed

import time


def get_html(times):
    time.sleep(times)
    print(f"get page {times} success")
    return times


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    # 可以通过submit 将执行的函数放入线程池当中, submit 是立即返回
    # task1 = executor.submit(get_html, 3)
    # task2 = executor.submit(get_html, 2)

    # done()方法判断是否完成结束
    # result() 获取返回的结果
    # print(task1.done())
    #
    # print(task1.result())

    urls = [5, 2, 4, 3]
    all_task = [executor.submit(get_html, i) for i in urls]
    for future in as_completed(all_task):  # as_completed 返回的是一个生成器
        data = future.result()
        print(data)

    # for data in executor.map(get_html, urls):
    #     print(data)

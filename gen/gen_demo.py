

def gen_test():
    x = 1
    yield x + 1
    yield x + 2
    yield x + 3


g1 = gen_test()  # g1 就是一个generator 对象


def echo(val=None):
    print("Begin...")
    try:
        while True:
            try:
                val = yield val
            except Exception as e:
                val = e
    finally:
        print("End...")


g2 = echo(1)
print(next(g2))
print(next(g2))
print(g2.send(2))
print(g2.close())
print(g2.send(1))  # StopIteration

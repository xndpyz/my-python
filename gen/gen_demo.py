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
# print(g2.send(1))  # StopIteration


from contextlib import contextmanager


@contextmanager
def file_manager(file):
    try:
        f = open(file, "w")
        yield f
    finally:
        f.close()


# with file_manager("test.py") as r:
#     r.write("111")


import click
@click.command()
@click.option('--count', default=3)
@click.option('--name', prompt='输入你的名字：')
def hello(count, name):
    for x in range(count):
        print(f"Hello {name}!")




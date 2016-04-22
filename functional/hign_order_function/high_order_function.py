# -*- coding: utf-8 -*-


# 编写高阶函数，就是让函数的参数能够接收别的函数。
def add(x, y, f):
    return f(x) + f(y)


print add(-1, 9, add)

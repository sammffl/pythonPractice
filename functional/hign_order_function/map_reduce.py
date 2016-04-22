# -*- coding: utf-8 -*-


# map 与列表生成器相类似
def f(x):
    return x * x


print map(f, range(1, 11))
print [x * x for x in range(1, 11)]


# reduce 把结果继续和序列的下一个元素做累计计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y


print reduce(add, range(1, 11))

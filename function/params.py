# -*- coding: utf-8 -*-


def power(x, n=2):
    """
    默认值
    :param x:
    :param n:
    :return:
    """
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def calc(*numbers):
    """
    可变参数
    :param numbers:
    :return:
    """
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc([1, 2, 3])
calc(1, 2, 3)


def person(name, age, **kw):
    """
    关键字参数
    :param name:
    :param age:
    :param kw:组装成字典
    :return:
    """
    print 'name:', name, 'age:', age, 'other:', kw


person('Bob', 35, city='Beijing')


def func(a, b, c=0, *args, **kw):
    """
    参数顺序必须是1.必选参数、2.默认参数、3.可变参数、4.关键字参数
    :param a:
    :param b:
    :param c:
    :param args:
    :param kw:
    :return:
    """
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)

# -*- coding: utf-8 -*-
import math


def func():
    """
    定义函数
    :return:
    """
    print 'x'


def nop():
    """
    空函数
    :return:
    """
    pass


# 函数返回多个值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print x, y
# 在返回多个值时实际返回tuple，返回tuple可以省略括号，
# 多个变量也可以接受tuple，按位置赋值给对应的值

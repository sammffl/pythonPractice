# -*- coding: utf-8 -*-


# filter
def is_odd(n):
    return n % 2 == 1


# 结果: [1, 5, 9, 15]
filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


def not_empty(s):
    return s and s.strip()


filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# 结果: ['A', 'B', 'C']

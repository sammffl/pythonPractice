# -*- coding: utf-8 -*-


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print sorted([36, 59, 8, 99, 12], reversed_cmp)

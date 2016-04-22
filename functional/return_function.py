# -*- coding: utf-8 -*-


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


l_sum = lazy_sum(1, 2, 3, 4, 5)
print l_sum()

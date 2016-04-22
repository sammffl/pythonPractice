# -*- coding: utf-8 -*-

# 生成器 generator
# 一个接一个生成 next
g = (x * x for x in range(10))
print g.next()

g = (x * x for x in range(10))
for n in g:
    print n


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


print fib(6)

for g in fib(6):
    print g

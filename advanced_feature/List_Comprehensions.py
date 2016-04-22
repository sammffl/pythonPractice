# -*- coding: utf-8 -*-

# 创建list的生成式
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]

# 两层循环
print [m + n for m in 'ABC' for n in 'XYZ']

# -*- coding: utf-8 -*-

# 条件判断 if elif else
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

# 循环
# 第一种 for...in...
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
# 第二种 while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
# range 生成序列 range(num)默认自然数递增序列；
# range(start,end,step)有起始、终止和间隔递增序列
print range(0, 100, 5)

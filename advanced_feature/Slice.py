# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 从0开始去，直到索引3为止，不包括索引3
print L[0:3]
print L[:3]

L = range(100)
print L[:21:2]
print L[::5]
print L[::] # 原样复制
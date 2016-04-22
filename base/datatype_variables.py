# -*- coding: utf-8 -*-

# 整数、浮点数 1.23  1.23e9
# 字符串  'abc' | 'I\'m \"OK\"!'
print 'I\'m \"OK\"!'
# r''  内部字符串不转义
#  '''...''' 多行内容  r'''...'''
print r'is \n'
print '''line1
line2
line3
'''
# Boolean True/False
print True
# 运算符 and / or / not
print True and False
# 空值 None
print None
# 变量
# b显示ABC，内存中创建一个ABC字符串 ，a指向ABC，b也指向ABC，
# 创建XYZ，a指向XYZ，b不变
a = 'ABC'
b = a
a = 'XYZ'
print b
# 常量 大写 PI=3.14

# -*- coding: utf-8 -*-

# list 列表-有序集合 索引方式获取元素从0开始 ，超出索引IndexError
# 列表也可以是二维或以上的列表
classmates = ['Michael', 'Bob', 'Tracy']
print len(classmates)  # 3
# 最后一个元素
print classmates[-1]
# append 追加到列表末尾
classmates.append('Adam')
# insert 插入到指定位置
classmates.insert(1, 'Jack')
# pop 删除末尾元素 或者指定元素pop(index)
classmates.pop()

# ===============================
# tuple 元祖 一经初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
# 定义只有一个元素的元祖，元素后面加上,以免被认为是数学意义上的括号
single = (1,)

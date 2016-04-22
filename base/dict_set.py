# -*- coding: utf-8 -*-

# dict 全称 dictionary 类似java中的map ，键-值(key-value)存储
# 内部存放数据和放入时的顺序无关
# 使用不可变对象作为key  eq：list无法作为key
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
# 添加
d['Adam'] = 67
# 修改
d['Adam'] = 74
# in 判断 key 是否存在
print 'Thomas' in d
# get 获取key对应的value没有返回None
# get(key,defaultValue)
d.get('Thomas', -1)
# pop删除key
d.pop('Bob')

# ===============
# set 一组key的集合，不存value
# set不能重复
# 创建一个set需要提供list
s = set([1, 2, 3])
# 添加 add
s.add(4)
# 删除 remove
s.remove(2)

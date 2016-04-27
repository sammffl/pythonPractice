# -*- encoding:utf-8 -*-

import os

path = os.path.dirname(os.path.realpath(__file__))
print path
_path = os.path.join(path, "config")
print _path
config = {}
execfile(_path, config)

print config


# 装饰器


def log(func):
    def wrapper(*args, **kw):
        try:
            print 'begin %s():' % func.__name__
            return func(*args, **kw)
        except Exception, e:
            raise e
        finally:
            print 'end'

    return wrapper


# 相当于 now = log(now)
@log
def now():
    print '2016'
    return 2016


now = now()
print now


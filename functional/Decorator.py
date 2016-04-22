# -*- coding: utf-8 -*-
import functools


# 装饰器


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)

    return wrapper


# 相当于 now = log(now)
@log
def now():
    print '2016'


now()


# ================================
def log_high(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)

        return wrapper

    return decorator


#  now = log('execute')(now)
@log_high('execute')
def now_high():
    print '2016'


now_high()
print now_high.__name__


# =================================
# begin end


def log_mixed(param):
    if isinstance(param, str):
        # 是字符串
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print ' %s %s ' % (param, func.__name__)
                return func(*args, **kw)

            return wrapper

        return decorator
    else:
        def wrapper(*args, **kw):
            print '%s' % param.__name__
            return param(*args, **kw)

        return wrapper


@log_mixed
def now_1():
    print '2016'
    return 'now_1'


@log_mixed("test")
def now_2():
    print '2016'


print '======================='
ss = now_1()
now_2()

print ss

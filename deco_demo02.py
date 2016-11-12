# coding=utf-8
def deco(arg):
    def _deco(func):
        def __deco():
            print 'before %s called %s' %(func.__name__, arg)
            func()
            print 'after %s called [%s]' %(func.__name__, arg)
        return __deco
    return _deco

@deco('module1')   # 装饰器中传入字符串
def myfunc1():
    print 'myfunc1 called'

@deco('module2')
def myfunc2():
    print 'myfunc2 called'

myfunc1()
myfunc2()

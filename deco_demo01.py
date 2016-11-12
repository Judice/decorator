# coding=utf-8
def deco(func):
    def _deco(*args, **kwargs):
        print "before %s.called" % func.__name__
        res = func(*args,**kwargs)         # 此处一定要传递参数
        print "after %s.called and result is %s" % (func.__name__, res)
    return _deco

@deco
def myfunc1(a, b):
    print "myfunc1(%s,%s).called" %(a,b)
    return a+b

@deco
def myfunc2(a,b,c):
    print "myfunc2(%s,%s,%s).called" %(a,b,c)
    return a+b+c

myfunc1(1,2)
myfunc2(1,2,3)

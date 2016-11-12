# coding=utf-8
class locker():                                   # 装饰器带类参数
    def __init__(self):
        print 'locker.__init__ should not be called'

    @staticmethod
    def acquire():
        print 'locker.acquire called'

    @staticmethod
    def release():
        print 'locker.release called'

def deco(cls):
    # cls 必须实现acquire和release静态方法
    def _deco(func):
        def __deco():
            print 'before %s called [%s]' % (func.__name__ , cls)
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco(locker)
def myfunc():
    print 'myfunc called'

myfunc()

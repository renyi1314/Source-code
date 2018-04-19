class SayMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['say_'+name] = lambda self,value,saying=name: print(saying+','+value+'!')
        return type.__new__(cls, name, bases, attrs)


class Hello(object, metaclass=SayMetaClass):
    pass
class hehe(object,metaclass=SayMetaClass):
    pass
# 二生三：创建实列
# hello = Hello()

# 三生万物：调用实例方法
# hello.say_Hello('world!')

a = hehe()
a.say_hehe("wqe")
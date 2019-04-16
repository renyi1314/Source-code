# 道生一：传入type
class SayMetaClass(type):

    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name, bases, attrs):
        # 创造“天赋”
        attrs['say_' + name] = lambda self, value, saying=name: print(saying + ',' + value + '!')
        # 传承三大永恒命题：类名称、父类、属性
        return type.__new__(cls, name, bases, attrs)


# 一生二：创建类
class Hello2(object, metaclass=SayMetaClass):
    pass


# 二生三：创建实列
hello2 = Hello2()

# 三生万物：调用实例方法
hello2.say_Hello2('world!')

print(dir(hello2))
print(hello2.__dict__)
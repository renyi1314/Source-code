"""
    单例模式: 一个类有且只能创建一个实例对象空间

"""
class Singleton(object):
    #保存创建的对象空间
    __instance = None
    #是否初始化
    __has_init = False
    # 创建对象空间
    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            # print(cls.__instance)  #这里面为什么不能打印开辟的空间地址？
            print(dir(cls))
            print(cls.__instance)
        return cls.__instance
    def __init__(self,name,age):
        if Singleton.__has_init == False:
            self.__name = name
            self.__age = age
            # print(self.__name)
            # print(self.__instance)
            Singleton.__has_init = True
    def __str__(self):
        # msg = "我是%s，今年%s岁"%(self.__name,self.__age)
        msg = "hello"
        return msg

stu_a = Singleton("大乔",18)
# print(Singleton._Singleton__instance)
# print(stu_a)
# stu_b = Singleton("小乔",17)
# print(stu_b)
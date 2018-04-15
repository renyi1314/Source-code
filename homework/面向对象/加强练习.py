# 1.请简单解释python中的static method(静态方法)和class method(类方法)，并任意写一个类包含静态方法和类方法，并且调用它们。
# 静态方法将函数封装在类中,不适用任何类或实例的参数
# 类方法由类调用,且第一个参数为cls


class ClassStaticMethod:
    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass


a = ClassStaticMethod()
# 调用类方法
ClassStaticMethod.class_method()
# 调用静态方法
ClassStaticMethod.static_method()
'''
    2.请完成以下函数将rpstr中的oldStr替换成newStr
class Tool(object):
    @staticmethod
    def strreplace(rpstr,oldStr,newStr):
        """将rpstr中的oldStr替换成newStr"""
        pass
例如： 将 "hello world! hello world!"中的world替换成 Tom
'''


class Tool(object):
    @staticmethod
    def strreplace(rpStr, oldStr, newStr):
        rpStrNew = rpStr.replace(oldStr, newStr)
        return rpStrNew


toola = Tool()
print(toola.strreplace("hello world! hello world!", "world", "Tom"))

# 3.每一个python的_函数_都可以被当作一个模块，导入模块使用_import_


'''
    4.所有python对象都有三个重要的特性：______、______、_______
'''
# 继承,封装,多态
'''
    5.python的标准内建函数有_____、_____、______、______、______等
'''


# __init__,__new__,__str__,__del__,__dict__
# 6.在 Python 中,类和对象有什么区别?对象如何访问类的方法? 创建一个对象时做了什么?
# 类为一类对象的总称,对象为类的实体,直接访问或者通过类访问,执行了__new__创建对象,__init__初始化对象的属性

# 7.请写出一段 Python 代码实现删除一个 list 里面的重复元素
def listQuchong(list_tmp):
    return list(set(list_tmp))


# 8.写出一个函数,给定参数 n,生成含有 n 个元素值为 1~n 的数 组,元素顺序随机,但值不重复
import random


def random_num(num):
    num_list = []
    for i in range(num):
        num_list.append(random.randint(1, 100))
    return num_list


print(listQuchong(random_num(100)))

# 9.在不用其他变量的情况下，交换a、b变量的值
a = 1
b = 2
a, b = b, a

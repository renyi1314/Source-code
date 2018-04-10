"""
名片管理系统:

1. 运行开始时: 显示主菜单

2. 根据菜单上的数字执行相应的操作:
    2.1 新建名片(1)
    2.2 显示全部(2)
    2.3 查询名片(3)
    2.4 退出系统(0)


2. 新建名片
    2.1 提示用户输入名片信息(姓名,电话,QQ号,邮箱)
    2.2 保存后到主菜单

    编程思路: 将上面的信息保存到字典中,  字典保存到列表中

3. 显示全部
   编程思路:  将列表中每个名片(字典)显示出来

4. 查询名字:
    4.1 提示请输入要搜索的名字
    4.2 搜索出来的内容显示出来

    编程思路:
    循环出每个列表中的字典(名片), 使用名字和每个字典(名片)的名字进行对比

    4.3 提示对找到的内容操作的菜单.
        请选择要执⾏的操作 [1] 修改 [2] 删除 [0] 返回上级菜单

5. 修改:
    5.1 提示需要输入的修改数据.
    5.2 使用这些数据将找到的名片内容修改掉.

6. 删除:
   编程思路: 将找到的名片信息从列表中删除



7. 编程要求:
    将以上每个功能封装到函数中.
"""

lis_card_info = []  #新建一个列表,存放字典方便操作

def login():
    """
    登录界面函数功能块
    :return:密码与账号正确,返回 主菜单界面
    """
    for num in range(0, 3):     #计数,只能输错三次
        a = str(input("请输入账号:"))    #从键盘输入账号
        p = str(input("请输入密码:"))    #从键盘输入密码
        if a == "1" and p == "1":   #判断账号密码是否正确
            print("登录成功!")
            return show_menu()
        else:   #输入错误后的操作
            if num == 2:
                print("账号已锁定,24小时后解锁")
            else:
                print("账号或密码错误,请重新输入")


def show_menu():
    """
    名片主菜单功能
    :return: 没有返回值
    """
    print("=" * 50)
    print()
    print("欢迎来到名片系统!")
    print("根据菜单上的数字执行相应的操作")
    print("1 新建名片")
    print("2 显示全部")
    print("3 查询名片")
    print("0 退出系统")


def creat_card():
    """
    输入1后:创建新名片功能
    :return: 无返回
    """
    print("欢迎来到新建名片界面!")
    while True:     #如果输入为空,则一直循环
        new_name = str(input("请输入姓名:"))
        if new_name == "":      #判断是否输入为空
            print("不能为空,请重新输入!")
        else:
            break

    while True:     #如果输入为空,则一直循环
        new_tel = str(input("请输入电话:"))
        if new_name == "":      #判断是否输入为空
            print("不能为空,请重新输入!")
        else:
            break

    while True:     #如果输入为空,则一直循环
        new_qq = str(input("请输入qq:"))
        if new_name == "":      #判断是否输入为空
            print("不能为空,请重新输入!")
        else:
            break

    while True:     #如果输入为空,则一直循环
        new_email = str(input("请输入邮箱:"))
        if new_name == "":      #判断是否输入为空
            print("不能为空,请重新输入!")
        else:
            break

    dic_infor = {}  #新建一个字典,存储名片信息

    dic_infor["name"] = new_name
    dic_infor["tel"] = new_tel
    dic_infor["qq"] = new_qq
    dic_infor["email"] = new_email
    lis_card_info.append(dic_infor)     #将字典放入列表中
    print()
    print("新建成功!")
    print()
    print(lis_card_info)


def show_card():
    """
    实现查看名片内容的功能
    :return: 无返回值
    """
    print("*欢迎来到查看界面!*")
    print()
    print("名字", end="\t")
    print("电话", end="\t")
    print("QQ", end="\t")
    print("邮箱", end="\t")
    print()
    for look in lis_card_info:      #遍历名片列表
        print(look["name"], look["tel"], look["qq"], look["email"])


def query_card():
    """
    实现查询名片功能,其中包括修改,删除功能
    :return: 无返回值
    """
    print("*欢迎来到查询界面*")
    print()
    query_name = str(input("请输入查询姓名:"))
    for i in lis_card_info:     #遍历名片列表
        if query_name == i["name"]:     #判断输入的姓名是否与名片列表中的姓名一致
            print("名字", end="\t")
            print("电话", end="\t")
            print("QQ", end="\t")
            print("邮箱", end="\t")
            print()
            print(i["name"], i["tel"], i["qq"], i["email"])
            while True:     #循环判断输入值是否为y或者n
                revise = str(input("修改y            删除n"))
                if revise == "y":
                    while True:
                        i["name"] = str(input("新的名字:"))
                        if i["name"] == "":
                            print("不能为空,重新输入!")
                        else:
                            break

                    while True:     #循环判断输入值是否为空
                        i["tel"] = str(input("新的电话:"))
                        if i["tel"] == "":
                            print("不能为空,重新输入!")
                        else:
                            break

                    while True:     #循环判断输入值是否为空
                        i["qq"] = str(input("新的qq:"))
                        if i["qq"] == "":
                            print("不能为空,重新输入!")
                        else:
                            break

                    while True:     #循环判断输入值是否为空
                        i["email"] = str(input("新的邮箱:"))
                        if i["email"] == "":
                            print("不能为空,重新输入!")
                        else:
                            break
                    print("修改成功!")
                    break

                elif revise == "n":
                    lis_card_info.remove(i)
                    print("删除成功!")
                    break
                else:
                    print("输入错误,请重新输入!")
        else:
            print("查无此人,请检查是否输入正确!")


def administrator():
    """
    实现功能键控制别的功能函数的作用
    :return: 无返回值
    """
    login()     #调用登录函数
    while True:     #一直循环检测操作
        control_num = str(input("请输入操作号:"))
        if control_num == "1":
            creat_card()

        elif control_num == "2":
            show_card()

        elif control_num == "3":
            query_card()

        elif control_num == "0":
            quit()
        else:
            print("输入错误!请重新输入")


administrator()












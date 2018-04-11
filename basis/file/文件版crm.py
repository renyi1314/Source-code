"""
1. 学习目标
    通过crm的综合练习对知识点全面掌握

2. 需求:
      1. 可维护一张客户信息表(客户表字段有：客户编号，姓名，性别，qq，电话)--使用文件存储客户信息
          客户编号|姓名|性别|qq|电话
          客户编号|姓名|性别|qq|电话
      2.操作选项提示：1 增加客户  2 删除客户 3 查询客户信息 4 显示列表
"""
import os

print("操作选项：1、显示所有客户信息 2、查询客户信息 3、增加客户 4、删除客户 5、按5或q退出")

while True:
    op = input("请输入操作选项编号：")
    if op == "1":
        f = open("user.txt", "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            print(line.replace("|", "   "))
        f.close()
    elif op == "2":
        id = input("请输入客户id:：")
        f = open("user.txt", "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            infos = line.split("|")  # 得到一个客户信息
            if id == infos[0]:  # 查看id是否一致
                print(line.replace("|", "   "))
        f.close()

    elif op == "3":
        userid = input("请输入客户id:")
        username = input("请输入客户姓名:")
        sex = input("请输入客户性别:")
        qq = input("请输入客户qq:")
        phone = input("请输入客户电话:")
        f = open("user.txt", "a", encoding="utf-8")
        f.write("%s|%s|%s|%s|%s\n" % (userid, username, sex, qq, phone))
        f.close()

    elif op == "4":
        userid = input("请删除的客户id:")
        f = open("user.txt", "r", encoding="utf-8")
        swap = open("user.swap.txt", "a", encoding="utf-8")  # 临时文件
        lines = f.readlines()
        for line in lines:
            infos = line.split("|")  # 得到一个客户信息
            if userid == infos[0]:  # 查看id是否一致,过滤掉不需要的数据
                continue
            swap.write(line)  # 写在临时文件中
        swap.close()
        f.close()
        os.remove("user.txt")
        os.rename("user.swap.txt", "user.txt")

    elif op == "5" or op == "q":
        print("退出CRM系统!")
        break

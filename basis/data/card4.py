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
print("操作提示1[增加客服] 2[删除客户] 3[查询客户信息] 4[显示列表]")
while True:
    action = input("请选择您的操作:")
    if action == "1":
        id = input("请输入客户编号")
        name = input("请输入客户名")
        sex = input("请输入客户性别")
        qq = input("请输入客户qq")
        tel = input("请输入客户电话")
        f = open("客户信息.txt", "a", encoding="utf-8")
        f.write("%s|%s|%s|%s|%s\n" % (id,name,sex,qq,tel))
        f.close()
        print("添加成功")
    elif action == "2":
        userid = input("请删除的客户id:")
        f = open("客户信息.txt", "r", encoding="utf-8")
        a = open("临时.txt","a",encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            infos = line.split("|")
            if userid == infos[0]:
                continue
            a.write(line)
        f.close()
        a.close()
        os.remove("客户信息.txt")
        os.rename("临时.txt","客户信息.txt")
    elif action == "3":
        id = input("请输入客户id:：")
        f = open("客户信息.txt", "r", encoding="utf-8")
        lines = f.readlines()
        for line in lines:
            infos = line.split("|")
            if id == infos[0]:
                print(line.replace("|", "   "))
        f.close()
    elif action == "4":
        f = open("客户信息.txt", "r", encoding="utf-8")
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line, end="")
        f.close()
    elif action == "0" :
        print("退出系统!")
        break
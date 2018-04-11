import re
import os

'''
需求:
        1、显示所有客户信息 
        2、查询客户信息 
        3、增加客户 
        4、删除客户 
        5、按5或q退出
'''


def input_info():
    user_id = input("请输入ID: ")
    name = input("请输入名字: ")
    while True:
        if re.findall("^[\\u4e00-\\u9fa5]{2,4}$", name):
            break
        else:
            name = input("请输入正确的姓名: ")
    phone = input("请输入电话: ")
    while True:
        if re.findall("^1[34578]\d{9}$", phone):
            break
        else:
            phone = input("请输入正确的电话: ")
            continue
    QQ = input("请输入QQ号: ")
    while True:
        if re.findall("^\d{6,11}$", QQ):
            break
        else:
            QQ = input("请输入正确的QQ号: ")
            continue
    email = input("请输入邮箱: ")
    while True:
        if re.findall("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
            break
        else:
            email = input("请输入正确的邮箱地址: ")
            continue
    return user_id + "|" + name + "|" + phone + "|" + QQ + "|" + email


def main():
    print("系统帮助     \n[1]显示所有客户信息\n[2]查询客户信息\n[3]增加客户\n[4]删除客户\n[5]按5或q退出")
    choice = input("请选择操作:")
    while True:
        if choice in ["1", "2", "3", "4", "5", "q"]:
            break
        else:
            choice = input("请选择正确的操作: ")
    if choice == "1":
        display_all()
    elif choice == "2":
        search_user_by_id()
    elif choice == "3":
        register()
    elif choice == "4":
        del_user()
    elif choice in ["5", "q"]:
        quit_fn()


def display_all():
    with open("crm_user.txt", mode="r", encoding="utf-8)") as f:
        for line in f.readlines():
            print(line.replace("|", "\t"))
    main()


def search_user_by_id():
    tmp_id = input("请输入要查找的id: ")
    with open("crm_user.txt", mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            if tmp_id == line.rstrip("\n").split("|")[0]:
                print(line.replace("|", "\t"))


def register():
    with open("crm_user.txt", mode="a", encoding="utf-8") as f:
        f.write(input_info() + "\n")
    print("信息添加成功! ")


def del_user():
    tmp_id = input("请输入要删除客户的id: ")
    with open("crm_user.txt", mode="r", encoding="utf-8") as f, open("crm_user_bak.txt", mode="w",
                                                                     encoding="utf-8") as f_bak:
        for line in f.readlines():
            print(line)
            if tmp_id == line.rstrip("\n").split("|")[0]:
                pass
            else:
                f_bak.write(line)
    os.remove("crm_user.txt")
    os.rename("crm_user_bak.txt", "crm_user.txt")


def quit_fn():
    print("退出系统! ")


while True:
    main()

import re
card_list = []


def main():
    print("欢迎进入名片管理系统")
    print("请选择操作:  ")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查找名片")
    print("0.退出系统")
    choice = input("请输入选择的操作")
    if choice == "1":
        insert_card()
    elif choice == "2":
        display_all_card()
    elif choice == "3":
        search_card_by_name()
    elif choice == "0":
        print("退出操作")
    else:
        print("请选择正确的操作")
        main()


def insert_card():
    name = input("请输入名字: ")
    phone = input("请输入电话: ")
    if is_phone_num(phone):
        QQ = input("请输入QQ号: ")
        email = input("请输入邮箱: ")
        card_list.append({"name": name, "phone": phone, "QQ": QQ, "email": email})
        print("新建成功")
        main()


def display_all_card():
    print("名字\t\t电话\t\tQQ\t\t邮箱")
    for card in card_list:  # 遍历列表,获取所有字典
        print("{name}\t{phone}\t{QQ}\t{email}".format(**card))  # 打印字典所有值
        print()
    main()


def search_card_by_name():
    tmp_name = input("请输入要查询的名字: ")
    for card in card_list:
        if tmp_name == card["name"]:
            print("名字\t\t电话\t\tQQ\t\t邮箱")
            print("{name}\t{phone}\t{QQ}\t{email}".format(**card))
            print()
            choice = input("请选择要执⾏的操作 [1] 修改 [2] 删除 [0] 返回上级菜单")
            if choice == "1":
                update_search_card(card)
            elif choice == "2":
                delete_search_card(card)
            elif choice == "0":
                main()
        else:
            print("没有找到相应的名字")


def update_search_card(card):
    name = input("请输入名字: ")
    phone = input("请输入电话: ")
    QQ = input("请输入QQ号: ")
    email = input("请输入邮箱: ")
    card["name"] = name
    card["phone"] = phone
    card["QQ"] = QQ
    card["email"] = email
    print("数据修改成功")
    main()

'''
正则表达模块,判断用户输入是否合法
'''
def is_phone_num(num):
    match_mub = re.findall("^1[34578]\d{9}$", num)
    if match_mub:
        return True
    else:
        return False

def delete_search_card(card):
    card_list.remove(card)
    print("数据删除成功")
    main()


main()

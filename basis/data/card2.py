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
    card_list.append(input_info())
    print("新建成功")
    main()


def display_all_card():
    if len(card_list) == 0:
        print("没有任何数据!!!!!!!!")
    else:
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
                continue
    else:
        print("没有找到相应的名字")
        main()


def update_search_card(card):
    card.update(input_info())
    print("数据修改成功")
    main()


# 获取用户输入,并判断是否非法
def input_info():
    name = input("请输入名字: ")
    while True:
        match_name = re.findall("^[\\u4e00-\\u9fa5]{2,4}$", name)
        if match_name:
            break
        else:
            name = input("请输入正确的姓名: ")
    phone = input("请输入电话: ")
    while True:
        match_nub = re.findall("^1[34578]\d{9}$", phone)
        if match_nub:
            break
        else:
            phone = input("请输入正确的电话: ")
            continue
    QQ = input("请输入QQ号: ")
    while True:
        match_qq = re.findall("^\d{6,11}$", QQ)
        if match_qq:
            break
        else:
            QQ = input("请输入正确的QQ号: ")
            continue
    email = input("请输入邮箱: ")
    while True:
        match_email = re.findall("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email)
        if match_email:
            break
        else:
            email = input("请输入正确的邮箱地址: ")
            continue
    return {"name": name, "phone": phone, "QQ": QQ, "email": email}


def delete_search_card(card):
    card_list.remove(card)
    print("数据删除成功")
    main()


if __name__ == "__main__":
    main()

'''
需求:1,显示用户菜单
'''
card_list = []
tmp_card = {}       # 临时保存查找到的数据
tmp_name = ""       # 临时保存查找的名字
tmp_index = int()   # 临时保存查找到数据的索引,用于更新数据


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
    QQ = input("请输入QQ号: ")
    email = input("请输入邮箱: ")
    card_list.append({"name": name, "phone": phone, "QQ": QQ, "email": email})
    print("新建成功")
    main()


def display_all_card():
    print("名字\t\t电话\t\tQQ\t\t邮箱")
    for card in card_list:  # 遍历列表,获取所有字典
        print("{name}\t{phone}\t{QQ}\t{email}".format(**card))  # 打印字典所有值
        # for value in card.values():
        #     print(value, end="\t")
        print()
    main()


def search_card_by_name():
    tmp_name = input("请输入要查询的名字: ")
    for card in card_list:
        tmp_card = card
        tmp_index = card_list.index(tmp_card)
        if tmp_name == card["name"]:
            print(tmp_index)
            print("名字\t\t电话\t\tQQ\t\t邮箱")
            print("{name}\t{phone}\t{QQ}\t{email}".format(**card))
            # for value in card.values():
            #     print(value, end="\t")
            print()
            choice = input("请选择要执⾏的操作 [1] 修改 [2] 删除 [0] 返回上级菜单")
            if choice == "1":
                update_search_card()
            elif choice == "2":
                delete_search_card()
            elif choice == "0":
                main()
    else:
        print("没有找到相应的名字")
        main()


def update_search_card():
    name = input("请输入名字: ")
    phone = input("请输入电话: ")
    QQ = input("请输入QQ号: ")
    email = input("请输入邮箱: ")
    tmp_card["name"] = name
    tmp_card["phone"] = phone
    tmp_card["QQ"] = QQ
    tmp_card["email"] = email
    card_list[tmp_index] = tmp_card
    print("数据修改成功")
    print(tmp_index)
    main()


def delete_search_card():
    del card_list[tmp_index]
    print("数据删除成功")
    main()


main()

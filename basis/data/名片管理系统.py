def show_menu():
    """
    显示菜单
    """
    print("*" * 50)
    print("欢迎使⽤【菜单管理系统】V1.0")
    print("")
    print("1. 新建名⽚")
    print("2. 显示全部")
    print("3. 查询名⽚")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_car():
    print("-" * 50)
    print("功能：新建名⽚")

    # 1. 提示⽤户输⼊名⽚信息
    name = input("请输⼊姓名：")
    phone = input("请输⼊电话：")
    qq = input("请输⼊ QQ 号码：")
    email = input("请输⼊邮箱：")
    # 2. 将⽤户信息保存到⼀个字典
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    # 3. 将⽤户字典添加到名⽚列表
    card_list.append(card_dict)
    print(card_list)
    # 4. 提示添加成功信息
    print("成功添加 %s 的名⽚" % card_dict["name"])


def search_card():
    """搜索名⽚
    """
    print("-" * 50)
    print("功能：搜索名⽚")

    find_name = input("请输入要搜索的名字:")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("{name}\t{phone}\t{qq}\t{email}\t".format(**card_dict))
            deal_card(card_dict)
            break
    else:
        print("没有找到%s名片" % find_name)


def update_card(find_dict):
    find_dict["name"] = input("请输⼊姓名：")
    find_dict["phone"] = input("请输⼊电话：")
    find_dict["qq"] = input("请输⼊QQ：")
    find_dict["email"] = input("请输⼊邮件：")
    print("修改成功!")


def remove_card(find_dict):
    card_list.remove(find_dict)
    print("删除成功!")


def deal_card(find_dict):
    """操作搜索到的名⽚字典
    :param find_dict:找到的名⽚字典
    """
    print(find_dict)
    action = input("请选择要执⾏的操作 "
                   "[1] 修改 [2] 删除 [0] 返回上级菜单")
    if action in ["1", "2", "0"]:
        if action == "1":
            update_card(find_dict)
        elif action == "2":
            remove_card(find_dict)
        elif action == "0":
            return
    else:
        print("输入操作，请重新输入!")


def show_all():
    """显示全部
    """
    print("-" * 50)
    print("功能：显示全部")
    print()
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, "\t")

    if len(card_list) == 0:
        print("提示: 没有任何名片记录")
        return
    for card_dict in card_list:
        print("{name}\t{phone}\t{qq}\t{email}\t".format(**card_dict))


card_list = []
while True:
    # >>1. 现实菜单
    show_menu()

    # >>2. 选择功能
    action = input("请选择操作功能：")
    print("您选择的操作是：%s" % action)

    # >>3. 根据用户录入功能选项执行对应的功能
    if action in ["0", "1", "2", "3"]:
        if action == "1":
            new_car()
        elif action == "2":
            show_all()
        elif action == "3":
            search_card()
        elif action == "0":
            print("欢迎再次使用名片管理系统")
            break
    else:
        print("输入操作，请重新输入!")
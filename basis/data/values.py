card_list = [{'name': 'renyi', 'phone': '18109070604', 'QQ': '541421397', 'email': '541421397@qq.com'}]
dict_card = {'name': 'renyi', 'phone': '18109070604', 'QQ': '541421397', 'email': '541421397@qq.com'}
tmp_card = {}
tmp_name = ""
tmp_index = int()

def search_card_by_name():
    tmp_name = input("请输入要查询的名字: ")
    for card in card_list:
        tmp_card = card
        tmp_index = card_list.index(tmp_card)
        if tmp_name == card["name"]:
            for value in card.values():
                print(value, end="\t")
        else:
            print("没有找到相应的名字")
    print()

def update_search_card():
    name = input("请输入名字: ")
    phone = input("请输入电话: ")
    QQ = input("请输入QQ号: ")
    email = input("请输入邮箱: ")
    tmp_card["name"] = name
    tmp_card["phone"] = phone
    tmp_card["QQ"] = QQ
    tmp_card["eamil"] = email
    card_list[tmp_index] = tmp_card

search_card_by_name()
update_search_card()
print(card_list)
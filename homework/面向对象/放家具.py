class Home:

    def __init__(self, area_home):
        self.area_home = int(area_home)
        self.items = []
        self.light_status = True
        self.remain_area = int(area_home)

    def add_items(self, furniture):
        self.remain_area = self.area_home - furniture.area_fu
        self.items.append(furniture.name)

    def open_light(self):
        self.light_status = True

    def close_light(self):
        self.light_status = False

    def __str__(self):
        return "家的大小:{}平米,剩余空间:{},当前灯的状态:{},有家具:{}".format(self.area_home, self.remain_area, self.light_status,
                                                           self.items)


class Furniture:

    def __init__(self, name, area_fu):
        self.name = name
        self.area_fu = int(area_fu)
        self.visible = True

    def is_visible(self):
        if self.visible:
            self.visible = False
        else:
            self.visible = True


home = Home(1000)
print(home)
table = Furniture("桌子", 10)
home.close_light()
home.add_items(table)
print(home)
print(dir(home))
print(dir(table))

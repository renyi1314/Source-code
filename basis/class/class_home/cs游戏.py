'''
    人,枪,弹夹,子弹
'''


# 属性:人-警,匪
# 方法:开枪,换子弹(调用枪的方法)
class Person:

    def __init__(self, status, gun):
        self.status = status
        self.gun = gun

    def print_person_status(self):
        print("当前状态:{}  武器:{}  弹夹容量:{}弹夹还有{}发子弹,总子弹还剩{}".format(self.status, self.gun.name, self.gun.clip.rongliang,
                                                                self.gun.clip.cu_shuliang,
                                                                self.gun.clip.bullet.count))

    def change_the_bullet(self):
        self.gun.change_the_bullet()
        self.print_person_status()

    def open_fire(self, num):
        self.gun.clip.cu_shuliang = self.gun.clip.cu_shuliang - num
        # print("{}拿着{}开了{}枪,当前子弹:{},总子弹还剩{}".format(self.status, self.gun.name, num, self.gun.clip.cu_shuliang,
        #                                           self.gun.clip.bullet.count))
        print("开了{}枪,当前子弹:{},总子弹还剩{}".format(num, self.gun.clip.cu_shuliang,
                                             self.gun.clip.bullet.count))


# 属性:枪的名字(AK,M4等)
# 方法:换子弹
class Gun:
    def __init__(self, name, clip):
        self.clip = clip
        self.name = name

    def change_the_bullet(self):
        self.clip.add_bullet()


# 属性:弹夹容量,当前弹夹子弹数量,加了子弹的数量
# 加子弹(弹夹容量-当前弹夹子弹数量)
class Clip:
    def __init__(self, bullet):
        self.bullet = bullet
        self.rongliang = 30
        self.cu_shuliang = 30
        self.add_shuliang = self.rongliang - self.cu_shuliang

    def add_bullet(self):
        self.add_shuliang = self.rongliang - self.cu_shuliang
        self.cu_shuliang = 30
        self.bullet.count = self.bullet.count - self.add_shuliang
        print("换子弹成功,子弹还剩{}".format(self.bullet.count))


# 属性:子弹大小(5.56mm,7.62mm) 子弹数量:
class Bullet:

    def __init__(self):
        # self.status = status
        self.count = 180


bullet = Bullet()
clip = Clip(bullet)
gun = Gun("M4", clip)
person = Person("警察", gun)
person.print_person_status()
person.open_fire(5)
person.change_the_bullet()
person.open_fire(10)
person.change_the_bullet()

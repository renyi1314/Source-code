class ZiDingYiError(Exception):

    def __init__(self, msg, length):
        self.msg = msg
        self.length = length

    def __str__(self):
        return "输入的内容:{}长度不够,至少{}位".format(self.msg, self.length)


try:
    s = input("请输入内容")
    if len(s) < 4:
        raise ZiDingYiError(s, 4)
    # print(ZiDingYiError)
except ZiDingYiError as e:
    print(e)
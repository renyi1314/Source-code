import datetime

print(datetime.datetime.today().strftime("%Y,%m,%d %H,%M,"))
print(type(datetime.date.today()))

time_now = "2018/04/21 13:23"
print(datetime.date.today().strftime("%Y,%m"))
# 将字符串格式化成机器可读时间(指定y,m,d等)
time_p = datetime.datetime.strptime(time_now, "%Y/%m/%d %H:%M")
# 返回的是datetime类
print(type(time_p))
# 通过类打印时间
print(time_p)
# 将机器可读时间按相应格式转化成指定格式(人类可读)的字符串
time_f = time_p.strftime("%Y,%m,%d %H,%M,")
# 返回字符串
print(type(time_f))
# 打印字符串
print(time_f)

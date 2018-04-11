import datetime

# f = open("E:\githubproject\Source-code\\basis\\file\\test.txt", mode='a')
with open("E:\githubproject\Source-code\\basis\\file\\test.txt", mode='r+') as f:
    while True:
        line = f.readline()
        print("-------------------", line, end="")
        if line:
            print(line, end="")
        else:
            break
    # for i in range(100):
    #     f.write(str(datetime.datetime.now()))
    #     f.write("\b")
    #     f.seek(0)
# for line in f:
#     print(line)

# f = open("E:\githubproject\Source-code\\basis\\file\\test.txt", mode='a')
with open("E:\githubproject\Source-code\\basis\\file\\test.txt", mode='a') as f:
    for i in range(100):
        for i in range(100):
            f.write("test")
            f.write("\b")
# for line in f:
#     print(line)

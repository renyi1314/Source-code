def cp(path):
    filename = path[0:path.rindex(".")]  # 通过rindex方法取得.之前的字符串(即文件名)
    ext = path[path.rindex("."):]  # 通过rindex方法取得.之后的字符串(即文件后缀)
    with open(path, 'r') as f, open("%s_bak%s" % (filename, ext), 'w') as f_bak:
        while True:
            data = f.read(1024)
            f_bak.write(data)
            if not data:
                break


path = "E:\githubproject\Source-code\\basis\\file\\test.txt"
# path = path.replace("\\", "/")  # 将字符串中含\的转换为/,避免出现特殊字符转换错误的问题
# print(path)
# path = '/'.join(path.split('\\')) #与上方法类似,但是还无法转换特殊字符...
cp(path)

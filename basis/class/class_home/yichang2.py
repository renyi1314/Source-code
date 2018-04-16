import time

# time.sleep(2)

try:
    try:
        f = open("123.txt", "r")
        while True:
            data = f.readline()
            if len(data) == 0:
                break
            print(data)
            time.sleep(2)
    except Exception:
        print("hehe")
    finally:
        print("文件关闭了")
except FileNotFoundError as e:
    print(e, "文件找不到")
else:
    print("文件读取成功")
finally:
    print("操作完成")

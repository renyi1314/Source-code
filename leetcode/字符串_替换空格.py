def replace(str):
    res = ""
    for s in str:
        if s == " ":
            s = "%20"
        res += s
    print(str, res)


if __name__ == '__main__':
    replace("hello world")

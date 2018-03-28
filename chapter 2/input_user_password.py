def login(count):
    # count = 3
    a = input("please input a number")
    b = "renyi"
    if a == b:
        print("success")
    elif count <= 0:
        print("no more chance")
    else:
        count -= 1
        print("haisheng %d" % count)
        return login(count=count)


if __name__ == "__main__":
    login(count=3)

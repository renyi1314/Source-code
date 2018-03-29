# def login(count):
#     # count = 3
#     a = input("please input password")
#     b = "renyi"
#     if a == b:
#         print("success")
#     elif count <= 0:
#         print("no more chance")
#     else:
#         count -= 1
#         print("haisheng %d" % count)
#         return login(count=count)
#
#
# if __name__ == "__main__":
#     login(count=3)

count = 3
while True:
    password = input("please input password")
    auth = "renyi"
    if password == auth:
        print("Success")
        break
    else:
        count -= 1
        if count < 0:
            print("No more chance")
            break
        else:
            print("chance haisheng : %d " % count )

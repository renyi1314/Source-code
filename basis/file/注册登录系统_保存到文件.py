with open("crm_user.txt", mode="r", encoding="utf-8") as f, open("crm_user_bak.txt", mode="w",
                                                                  encoding="utf-8") as f_bak:
    while True:
        tmpline = f.readline()
        if not tmpline:
            break
        if id == tmpline:
            pass
        else:
            f_bak.write(tmpline)
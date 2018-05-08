file = "ifcfg-eth0"


def get_mac(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        dict_settings = {key.split("=")[0]: key.split("=")[1].strip() for key in f}
        return dict_settings["HWADDR"]


def copy_file(filename):
    with open(filename, mode="r", encoding="utf-8") as f, open(filename + "-bak", "w", encoding="utf-8") as f_bak:
        f_bak.write(f.read().replace("=", ":"))


if __name__ == '__main__':
    dict_file = get_mac("ifcfg-eth0")
    print(dict_file)
    copy_file(file)

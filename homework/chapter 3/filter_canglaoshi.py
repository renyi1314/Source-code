def filter_cang():
    name = input("Please input: ").replace("苍老师", "***").replace("东京热", "***")
    # if "苍老师" in name:
    #     name = name.replace("苍老师", "***")
    # if "东京热" in name:
    #     name = name.replace("东京热", "***")  #做判断再修改
    # name = name.replace("苍老师", "***").replace("东京热", "***")   #直接修改
    return name


if __name__ == "__main__":
    print(filter_cang())

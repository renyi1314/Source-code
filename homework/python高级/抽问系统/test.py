# with open("test.txt", "r", encoding="utf-8") as f:
#     dict_settings = {key.split("=")[0]: key.split("=")[1].strip("\" \n") for key in f}
#     # print(dict_settings)
# print(dict_settings)

# with open("test.txt", "r", encoding="utf-8") as f:
#     list_a = f.readlines()
#     print(list_a)
with open("systemconfig", "r", encoding="utf-8") as f:
    dict_settings = {key.split("=")[0]: key.split("=")[1].strip("\" \n") for key in f if not key.startswith("#")}
print(dict_settings)
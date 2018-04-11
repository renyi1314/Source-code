import os

# print(os.getcwd("./one"))
print(os.listdir("./one/"))

for file in os.listdir("./one/"):
    print(file)
    # os.rename("./one/"+file, "./one/"+"hehe"+file)
    os.rename("./one/"+file, "./one/"+file[1:])

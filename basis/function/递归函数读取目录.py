import os


def list_dir(dirname, deep):
    filenames = os.listdir(dirname)
    for filename in filenames:
        print("       " * deep, filename)
        if os.path.isdir(dirname + "/" + filename):
            list_dir(dirname + "/" + filename, deep + 1)


list_dir("E:/githubproject/Source-code", 0)

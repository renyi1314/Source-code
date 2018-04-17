import os


def rmdir(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        if os.path.isfile(dirname + "/" + filename):
            os.remove(dirname + "/" + filename)
        else:
            rmdir(dirname + "/" + filename)
    os.rmdir(dirname)


rmdir("./123")

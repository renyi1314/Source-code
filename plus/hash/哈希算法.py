import hashlib


def hash_file(path):
    with open(path, 'rb') as f:
        mobj = hashlib.sha256()
        while True:
            data = f.read(1024)
            if not data:
                break
            mobj.update(data)
        # data = f.read()
        # mobj.update(data)
    return mobj.hexdigest()


# mobj2 = hashlib.sha256()
# mobj2.update(b'123456')
# print(mobj2.hexdigest())

path = "F:/迅雷下载/pycharm-professional-2018.1.exe"
print(hash_file(path))
# a12ef1a65f32f2f70d63d7bf48060ef3a14e93208f94df84e367f09bad691079 *pycharm-professional-2018.1.1.exe

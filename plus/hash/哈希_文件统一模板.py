import hashlib


def hash_file(path):
    file_hash = hashlib.sha256()
    with open(path, 'rb') as f:
        data = f.read(1024 ** 3)
        while data:
            file_hash.update(data)
            data = f.read(1024 ** 3)
    return file_hash.hexdigest()


path_file = "F:/迅雷下载/pycharm-professional-2018.1.exe"
# path_file = "F:/迅雷下载/Python-3.6.4.tgz"

print(hash_file(path_file))
# a12ef1a65f32f2f70d63d7bf48060ef3a14e93208f94df84e367f09bad691079 *pycharm-professional-2018.1.1.exe

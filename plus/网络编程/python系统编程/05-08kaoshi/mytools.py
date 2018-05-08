import sys
import hashlib

filNames = sys.argv[1:]


def hash_file(file_path):
    for filename in file_path:
        file_sha256 = hashlib.sha256()
        file_md5 = hashlib.md5()
        with open(filename, 'rb') as f:
            data = f.read(1024)
            while data:
                file_sha256.update(data)
                file_md5.update(data)
                data = f.read(1024)
            print("{} :  ".format(filename))
            print("sha256 :  {}".format(file_sha256.hexdigest()))
            print("md5 :  {}".format(file_md5.hexdigest()))


if __name__ == '__main__':
    hash_file(filNames)

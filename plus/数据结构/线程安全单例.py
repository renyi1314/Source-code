import threading

lista = []


def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func


def Singleton(cls):
    instances = {}

    @synchronized
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def syssingle(func):
    func.__lock__ = threading.Lock()

    def decora(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return decora


def worker():
    single_test = test()
    print("id----> %s" % id(single_test))
    lista.append(id(single_test))


@Singleton
class test():
    a = 1


if __name__ == "__main__":
    task_list = []
    for one in range(10000):
        t = threading.Thread(target=worker)
        task_list.append(t)

    for one in task_list:
        one.start()

    for one in task_list:
        one.join()

print(set(lista))

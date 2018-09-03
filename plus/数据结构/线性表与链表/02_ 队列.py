class LIFO:
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if self.__list == []:
            return None
        self.__list.pop()

    def top(self):
        if self.__list == []:
            return None
        return self.__list[-1]

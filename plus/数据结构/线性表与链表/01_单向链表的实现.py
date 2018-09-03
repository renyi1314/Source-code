# 定义结点
class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self._next = next_node


class SingleLinkList:
    '''定义单链表'''

    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head is None

    # 添加元素到开头
    def add(self, item):
        node = Node(item, self.head)
        self.head = node

    def len(self):
        count, tmp_node = 0, self.head
        while tmp_node:
            count += 1
            tmp_node = tmp_node._next
        return count

    def get_item(self, i):
        tmp_index, tmp_node = 0, self.head
        while tmp_index < i:
            tmp_node = tmp_node._next
            tmp_index += 1
        return tmp_node.item


# 初始化空链表
a = SingleLinkList()
a.add("5")
a.add("4")
a.add("3")
a.add("2")
a.add("1")
print(a.is_empty())
print(a.len())
print(a.get_item(0))

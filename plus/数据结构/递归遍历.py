def print_BinTree_Node(node):
    if node is None:
        print("^", end="")  # 空树
        return

    print("(" + str(node.value), end="")
    print_BinTree_Node(node.left)
    print_BinTree_Node(node.right)
    print(")", end="")

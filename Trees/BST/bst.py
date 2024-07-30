class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, root, val):
        if not root:
            root = Node(val)
            return root

        if root.data > val:
            root.left = self.insert(root.left, val)
        elif root.data == val:
            raise ValueError("Node already exists")
        else:
            root.right = self.insert(root.right, val)

        return root

    def inorder(self, root, is_root=True):
        if not root:
            return
        self.inorder(root.left, False)
        print(root.data, end=" ")
        self.inorder(root.right, False)
        if is_root:
            print()

    def search(self, root, val):
        if not root:
            return False
        if root.data == val:
            return True
        elif root.data < val:
            return self.search(root.right, val)
        elif root.data > val:
            return self.search(root.left, val)
        return False


if __name__ == "__main__":

    arr = [5, 1, 3, 4, 2, 7]
    tree = BST()

    for i in arr:
        try:
            tree.root = tree.insert(tree.root, i)
        except ValueError as e:
            print(e)

    tree.inorder(tree.root)
    print("5", tree.search(tree.root, 5))
    print("4", tree.search(tree.root, 4))
    print("2", tree.search(tree.root, 2))
    print("1", tree.search(tree.root, 1))
    print("6", tree.search(tree.root, 6))

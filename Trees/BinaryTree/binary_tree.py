from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def build_with_preorder(self, arr):  # O(N)
        self.index = -1

        def helper(arr):
            self.index += 1
            index = self.index
            if index >= len(arr) or arr[index] == -1:
                return None
            node = Node(arr[index])
            node.left = helper(arr)
            node.right = helper(arr)
            return node

        self.root = helper(arr)

    def preorder(self, root):  # O(N)
        if not root:
            print(-1, end=" ")
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root, is_root=True):  # O(N)
        if not root:
            print(-1, end=" ")
            return
        self.inorder(root.left, False)
        print(root.data)
        self.inorder(root.right, False)
        if is_root:
            print()

    def postorder(self, root):  # O(N)
        if not root:
            print(-1, end=" ")
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def levelorder(self, root):  # O(N)
        d = deque()
        if not root:
            print("Tree is empty")
            return
        d.append(root)
        # d.append(None)
        # level = 0
        # print("Level ", level)
        # while len(d) > 0:
        #     node = d.popleft()
        #     if node is None:
        #         if len(d) != 0:
        #             d.append(None)
        #             print()
        #             level += 1
        #             print("Level ", level)
        #         else:
        #             break
        #     else:
        #         print(node.data, end=" ")
        #         if node.left:
        #             d.append(node.left)
        #         if node.right:
        #             d.append(node.right)
        # pass
        level = 0
        while len(d) != 0:
            print(f"Level {level}", end=" ")
            for _ in range(len(d)):
                node = d.popleft()
                print(node.data, end=" ")
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            level += 1
            print()

    def countNodes(self, root):  # O(N)
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def height(self, root):  # O(N)
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def search(self, root, target):
        if not root:
            return False
        if root.data == target:
            return True
        return self.search(root.left, target) or self.search(root.right, target)


if __name__ == "__main__":

    tree = BinaryTree()
    arr = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, -1]
    tree.build_with_preorder(arr)

    # print("Inorder Traversal of the Constructed Tree:")
    # tree.preorder(tree.root)
    # tree.levelorder(tree.root)
    print("total nodes", tree.countNodes(tree.root))
    print("total height ", tree.height(tree.root))
    print("search 6", tree.search(tree.root, 6))
    print("search 5", tree.search(tree.root, 5))

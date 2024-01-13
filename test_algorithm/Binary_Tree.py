# 이진트리 생성, 삽입, 삭제, 탐색
from sys import stdin
input = stdin.readline

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)


    def _insert_recursive(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert_recursive(root.left, data)
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert_recursive(root.right, data)


    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)


    def _delete_recursive(self, root, value):
        if root is None:
            return root
        if value < root.data:
            root.left = self._delete_recursive(root.left, value)
        elif value > root.data:
            root.right = self._delete_recursive(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self._get_min_value(root.right)
            root.right = self._delete_recursive(root.right, root.data)
        return root


    def _get_min_value(self, root):
        while root.left is not None:
            root = root.left
        return root.data


    def preorder_traversal(self):
        result = []
        self.preorder_recursive(self.root, result)
        return result


    def _preorder_recursive(self, root, result):
        if root is not None:
            result.append(root.data)
            self._preorder_recursive(root.left, result)
            self._preorder_recursive(root.right, result)

    def inorder_traversal(self):
        result = []
        self.inorder_recursive(self.root, result)
        return result


    def _inorder_recursive(self, root, result):
        if root is not None:
            self._inorder_recursive(root.left, result)
            result.append(root.data)
            self._inorder_recursive(root.right, result)


    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result


    def _postorder_recursive(self, root, result):
        if root is not None:
            self._postorder_recursive(root.left, result)
            self._postorder_recursive(root.right, result)
            result.append(root.data)


# tree = BinaryTree()

# while True:
#     try:
#         item = int(input())
#         tree.insert(item)
#     except:
#         break

# lst = tree.postorder_traversal()
# print(*lst, sep='\n')
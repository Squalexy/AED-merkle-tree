class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "%s -> %s" % (self.key, self.value)

    def insert(self, key, value):
        if key == self.key:
            return
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.insert(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.insert(key, value)

    def get(self, key):
        if key == self.key:
            return self.value
        elif key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.get(key)
        elif key > self.key:
            if self.right is None:
                return None
            else:
                return self.right.get(key)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def __str__(self):
        return "asd"

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.root.insert(key, value)

    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    def print2D(self):
        BinaryTree.print2DUtil(self.root, 0)

    @staticmethod
    def print2DUtil(root: Node, space):
        if root is None:
            return

        space += 10

        BinaryTree.print2DUtil(root.right, space)

        print()
        for i in range(10, space):
            print(end=" ")
        print(root)

        BinaryTree.print2DUtil(root.left, space)


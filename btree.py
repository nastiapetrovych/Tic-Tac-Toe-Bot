"""
Creates a tree
"""
from btnode import BTNode


class BTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, item):
        """Adds item to the tree."""

        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left is None:
                    node.left = BTNode(item)
                else:
                    recurse(node.left)
            elif node.right is None:
                node.right = BTNode(item)
            else:
                recurse(node.right)

        if self.isEmpty():
            self.root = BTNode(item)
        else:
            recurse(self.root)
        self.size += 1

    def isEmpty(self):
        """
        Returns bool if the tree is empty
        """
        return self.size == 0

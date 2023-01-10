class BinarySearchTree:
    # The node class is only visible to the BinarySearchTree class
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val

        def setVal(self, newVal):
            self.val = newVal

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self, newLeft):
            self.left = newLeft

        def setRight(self, newRight):
            self.right = newRight

        # Iterates through left and right children of a Node, yielding each one of them.
        def __iter__(self):
            if self.left is not None:
                for element in self.left:
                    yield element

            yield self.val

            if self.right is not None:
                for element in self.right:
                    yield element

    # initializer of the BinarySearchTree
    def __init__(self):
        self.root = None

    def insert(self, val):

        # a recursive function that I'll be using for implementing this tree but users
        # of our tree won't know about it and also they can't use it.
        def __insert(root, newVal):
            if root is None:
                return BinarySearchTree.__Node(newVal)

            if newVal < root.getVal():
                root.setLeft(__insert(root.getLeft(), newVal))
            else:
                root.setRight(__insert(root.getRight(), newVal))

            return root

        self.root = __insert(self.root, val)

    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()

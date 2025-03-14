from BinarySearchTree import BinarySearchTree


def testBinarySearchTree():
    rawInputs = input("Enter a list of numbers: ")
    inputsList = rawInputs.split()

    tree1 = BinarySearchTree()

    for x in inputsList:
        tree1.insert(float(x))

    for x in tree1:
        print(x)


if __name__ == '__main__':
    testBinarySearchTree()

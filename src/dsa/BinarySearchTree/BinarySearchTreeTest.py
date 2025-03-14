from BinarySearchTree import BinarySearchTree

if __name__ == '__main__':
    rawInputs = input("Enter a list of numbers: ")
    inputsList = rawInputs.split()

    tree1 = BinarySearchTree()

    for x in inputsList:
        tree1.insert(float(x))

    for x in tree1:
        print(x)

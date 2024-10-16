from dsa.Stack import Stack
from dsa.BinarySearchTree import BinarySearchTree
from dsa.LinkedList import LinkedList


def testStack():
    firstStack = Stack()
    for num in list(range(34)):
        firstStack.push(num)
    print(firstStack.pop())
    print(firstStack.pop())
    print(firstStack.pop())
    print(firstStack.pop())
    print(firstStack.pop())

    firstStack.push(-21)
    print(firstStack.peek())
    print(firstStack.pop())

    secondStack = Stack()
    secondStack.push(3)
    secondStack.pop()
    secondStack.peek()


def testLinkedList():
    my_linked_list = LinkedList(["7", "2", "9"])
    print(my_linked_list)


def testBinarySearchTree():
    rawInputs = input("Enter a list of numbers: ")
    inputsList = rawInputs.split()

    tree1 = BinarySearchTree()

    for x in inputsList:
        tree1.insert(float(x))

    for x in tree1:
        print(x)


if __name__ == '__main__':
    testStack()
    testLinkedList()
    testBinarySearchTree()

import Stack
from LinkedList import LinkedList


def test_stack():
    firstStack = Stack.Stack()
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

    secondStack = Stack.Stack()
    secondStack.push(3)
    secondStack.pop()
    secondStack.peek()


def test_linked_list():
    my_linked_list = LinkedList(["7", "2", "9"])
    print(my_linked_list)


if __name__ == '__main__':
    test_stack()
    test_linked_list()

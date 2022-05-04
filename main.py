import Stack


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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


if __name__ == '__main__':
    test_stack()

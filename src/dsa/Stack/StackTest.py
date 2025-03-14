from src.dsa.Stack.Stack import Stack


def stack_example1():
    example_stack = Stack()

    print(f"The head of an empty stack : {example_stack.top}")
    print("Lets add a couple of our favorite colors to this stack...")

    example_stack.push("red")
    example_stack.push("brown")
    example_stack.push("dark blue")
    example_stack.push("cyan")
    example_stack.push("pink")

    print("And now we empty our stack while reading it.")

    while example_stack.peek():
        print(example_stack.pop(), end=" -> ")

    print(f"\nNow, our stack is : {example_stack.top}")


if __name__ == '__main__':
    stack_example1()

from src.dsa.Stack.Stack import Stack
import queue

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

def lifo_que_example1():
    example_numbers_stack = queue.LifoQueue()
    print(f"Is our stack empty now ? {example_numbers_stack.empty()}")
    example_numbers_stack.put(1)
    example_numbers_stack.put(7)
    example_numbers_stack.put(4)
    example_numbers_stack.put(9)
    print(f"Is our stack empty now ? {example_numbers_stack.empty()}")

    print(f"Right now, the size of our stack is : {example_numbers_stack.qsize()}")
    print(f"top of our stack is : {example_numbers_stack.get()}")
    print(f"top of our stack is : {example_numbers_stack.get()}")
    print(f"top of our stack is : {example_numbers_stack.get()}")
    print(f"top of our stack is : {example_numbers_stack.get()}")

    print(f"Is our stack empty now ? {example_numbers_stack.empty()}")


if __name__ == '__main__':
    stack_example1()
    lifo_que_example1()

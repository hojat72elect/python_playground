class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")

        topIndex = len(self.items) - 1
        item = self.items[topIndex]
        del self.items[topIndex]
        return item

    def push(self, item):
        self.items.append(item)

    # looking into the item that we'll receive if we pop the stack.
    def peek(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to peek into an empty stack")

        topIndex = len(self.items) - 1
        return self.items[topIndex]

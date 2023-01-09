class Stack:

    # We're creating the stack with the help of a list.
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("It's impossible to pop an empty stack")

        topIndex = len(self.items) - 1
        item = self.items[topIndex]
        del self.items[topIndex]
        return item

    def push(self, item):
        self.items.append(item)

    # The intent fo [peek] is to be safer than [pop] so peeking into an empty stack shouldn't throw an error.
    def peek(self):
        if self.isEmpty():
            return None

        topIndex = len(self.items) - 1
        return self.items[topIndex]

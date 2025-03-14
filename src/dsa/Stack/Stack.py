class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node_data = self.top.data
            self.top = self.top.next
            return popped_node_data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

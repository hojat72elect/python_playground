class Node:
    """
    Node is the building block for a linked list.
    there are various data structures that use Node as their building block; but for the
    sake of simplicity, and in order to avoid coupling, I'm going to use this node, ONLY for
    linked list.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    # For debug purposes
    def __repr__(self):
        return self.data


class LinkedList:
    """
    I don't know why but looks like this LinkedList
    can only contain string values and nothing else
    """

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next_node = Node(data=element)
                node = node.next_node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next_node
        nodes.append("None")  # as a sign that linked list has finished.
        return " -> ".join(nodes)

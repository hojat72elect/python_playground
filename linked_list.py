"""
Node is the building block for a linked list.
"""


class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, nextNode):
        self.nextNode = nextNode

    # For debug purposes
    def __repr__(self):
        return self.data


"""
I don't know why but looks like this LinkedList
can only contain string values and nothing else
"""


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.nextNode = Node(data=element)
                node = node.nextNode

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.nextNode
        nodes.append("None")  # as a sign that linked list has finished.
        return " -> ".join(nodes)


def testLinkedList():
    my_linked_list = LinkedList(["7", "2", "9"])
    print(my_linked_list)


if __name__ == "__main__":
    testLinkedList()

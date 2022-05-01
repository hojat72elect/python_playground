"""
Node is the building block for a linked list.
"""


class __Node:
    def __init__(self, value, nextRef=None):
        self.value = value
        self.nextRef = nextRef

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.nextRef

    def setNext(self, nextRef):
        self.nextRef = nextRef

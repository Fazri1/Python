class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getSize(self):
        count = 0
        currentNode = self.head
        while currentNode is not None:
            count += 1
            currentNode = currentNode.next
        return count

    def check(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

    def add(self, newData):
        if self.head is None:
            self.head = Node(newData)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(newData)


myLinkedList = LinkedList()

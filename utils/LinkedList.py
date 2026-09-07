from utils.Node import Node


class LinkedList:
    def __init__(self, elements=None):
        self.head = None

        if elements:
            for element in elements:
                self.append(element)

    def getHead(self):
        return self.head

    def push(self, node):
        node.next = self.head
        self.head = node

    def pop(self):
        temp = self.head
        self.head = self.head.next
        return temp

    def append(self, data):

        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = Node(data)

    def display(self):
        current = self.head
        elements = []
        while current != None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    array = [20, 30]
    my_list = LinkedList(elements=array)
    my_list.display()

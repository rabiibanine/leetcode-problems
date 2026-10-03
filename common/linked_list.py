from typing import final, override

from common.node import ListNode


@final
class LinkedList:
    def __init__(self, head=None, elements: list[int] | None = None):
        self.head = head

        if elements:
            for element in elements:
                self.append(element)

    @override
    def __str__(self):
        values = []

        current = self.getHead()

        while current:
            values.append(str(current.val))
            current = current.next

        return " -> ".join(values)

    def getHead(self):
        return self.head

    def getNext(self):
        head = self.getHead()
        return None if not head else head.next

    def push(self, node):
        node.next = self.getHead()
        self.head = node

    def pop(self):
        temp = self.head
        self.head = self.getNext()
        return temp

    def append(self, data):

        if not self.head:
            self.head = ListNode(data)
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = ListNode(data)


if __name__ == "__main__":
    array = [20, 30]
    my_list = LinkedList(elements=array)
    print(my_list)

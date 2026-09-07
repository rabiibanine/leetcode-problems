from utils.LinkedList import LinkedList
from utils.Node import Node


class Solution:
    def reverseList(self, head):
        pointer = head
        reverse_list_head = None

        while pointer:
            temp = pointer.next
            pointer.next = reverse_list_head
            reverse_list_head = pointer
            pointer = temp

        return reverse_list_head

    def displayList(self, head):
        pointer = head
        elements = []
        while pointer != None:
            elements.append(str(pointer.data))
            pointer = pointer.next
        print(" -> ".join(elements) + " -> None")

    def test(self):
        linked_list = LinkedList([1, 2, 3, 4])
        list_head = linked_list.getHead()

        self.displayList(list_head)
        reversed_list = self.reverseList(list_head)
        self.displayList(reversed_list)


solution = Solution()

solution.test()

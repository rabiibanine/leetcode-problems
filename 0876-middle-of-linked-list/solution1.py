class Solution:
    def middleNode(self, head):
        middle = head
        current = head

        while current.next != None and current.next.next != None:
            current = current.next.next
            middle = middle.next

        return middle.next if current.next != None else middle

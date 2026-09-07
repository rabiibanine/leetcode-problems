class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return None
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head

    def displayList(self, head):
        pointer = head
        elements = []
        while pointer != None:
            elements.append(str(pointer.data))
            pointer = pointer.next
        print(" -> ".join(elements) + " -> None")

    def test(self):
        return 0


solution = Solution()

solution.test()

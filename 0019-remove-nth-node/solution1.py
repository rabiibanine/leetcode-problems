from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = self.getLength(head)

        if length == 1:
            return None

        prev = None
        pointer = head
        index = 1

        while pointer != None:

            if length == n and head != None:
                return head.next

            if index == length - n + 1 and prev != None:
                prev.next = pointer.next if pointer.next else None
                break

            prev = pointer
            pointer = pointer.next
            index += 1

        return head

    def getLength(self, head: Optional[ListNode]) -> int:

        length = 0
        pointer = head
        while pointer != None:
            length += 1
            pointer = pointer.next

        return length

    def printLinkedList(self, ll: Optional[(ListNode)]):
        arr = []
        while ll != None:
            arr.append(ll.val)
            ll = ll.next
        print(arr)

    def test(self):
        node3 = ListNode(3)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)

        self.printLinkedList(self.removeNthFromEnd(node1, 3))


solution = Solution()

solution.test()

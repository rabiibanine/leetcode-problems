from typing import Optional
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        first = True
        result = None
        previous = None
        while l1 != None or l2 != None or carry:
            l1CurrentNumber = l1.val if l1 != None else 0
            l2CurrentNumber = l2.val if l2 != None else 0
            newNumber = l1CurrentNumber + l2CurrentNumber + carry
            carry = 0
            lNew = ListNode(newNumber % 10)
            if first:
                result = lNew
                first = False
            if newNumber >= 10:
                carry += newNumber // 10
            if previous != None:
                previous.next = lNew
            previous = lNew
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        return result

    # for testing
    @staticmethod
    def printListNode(listNode: Optional[ListNode]):
        array = []
        while listNode != None:
            array.append(listNode.val)
            listNode = listNode.next
        print(array)

    def createLLFromArray(self, array: List[int]):
        next = None
        array_length = len(array)
        for i in range(-1, -array_length - 1, -1):
            lNew = ListNode(array[i], next)
            next = lNew
        return next

    def test(self):
        l1 = self.createLLFromArray([9, 9, 9, 9, 9, 9, 9])
        l2 = self.createLLFromArray([9, 9, 9])
        lNew = self.addTwoNumbers(l1, l2)
        self.printListNode(lNew)


solution = Solution()

solution.test()

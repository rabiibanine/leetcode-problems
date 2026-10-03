from common.linked_list import LinkedList
from common.node import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        if not list1 or not list2:
            return list1 or list2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def test(self):
        list1 = LinkedList(elements=[1, 3, 5])
        list2 = LinkedList(elements=[2, 4, 6])

        print(LinkedList(self.mergeTwoLists(list1.getHead(), list2.getHead())))


solution = Solution()

solution.test()

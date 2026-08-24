from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        final_list = None
        final_list_pointer = None

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        # Initialization
        if list1.val < list2.val:
            final_list = list1
            list1 = list1.next
        else:
            final_list = list2
            list2 = list2.next

        final_list_pointer = final_list

        # Access issue, I tend to get into these a lot I should look for an optimal solution
        # The loop shouldn't be a thing since we advance list1 with its next
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                final_list_pointer.next = list1
                final_list_pointer = final_list_pointer.next
                list1 = list1.next
            else:
                final_list_pointer.next = list2
                final_list_pointer = final_list_pointer.next
                list2 = list2.next

        # Here the access issue could be solved by just putting the final nodes in the non null list right at the end of the final list
        if list1 != None:
            final_list.next = list1
        else:
            final_list.next = list2

        return final_list

    def printListNode(self, list1):
        array = []
        while list1 != None:
            array.append(list1.val)
            list1 = list1.next
        print(array)

    def test(self):
        node4 = ListNode(7)
        node3 = ListNode(5, node4)
        node2 = ListNode(3, node3)
        node1 = ListNode(1, node2)

        node8 = ListNode(8)
        node7 = ListNode(6, node4)
        node6 = ListNode(4, node3)
        node5 = ListNode(2, node2)

        listyboi = self.mergeTwoLists(node1, node5)
        self.printListNode(listyboi)


solution = Solution()

solution.test()

from typing import final


@final
class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


@final
class ListNode:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next

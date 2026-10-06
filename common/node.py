from typing import final


@final
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


@final
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


@final
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

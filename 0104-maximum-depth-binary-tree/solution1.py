from common.node import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

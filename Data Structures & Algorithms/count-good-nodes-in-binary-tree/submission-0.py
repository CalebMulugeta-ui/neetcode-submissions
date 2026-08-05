# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        final = 0
        def dfs(root, currentMax):
            if not root:
                return 0

            if root.val >= currentMax:
                final = 1
            else:
                final = 0

            currentMax= max(currentMax, root.val)

            final += dfs(root.left, currentMax) + dfs(root.right, currentMax)

            return final

        return dfs(root, root.val)
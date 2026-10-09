# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, sort):
            #base case
            if not root:
                return
            

            left = dfs(root.left, sort)
            sort.append(root.val)
            right = dfs(root.right, sort)

            return sort
        
        sortL = []
        sortL = dfs(root, sortL)
        
        
        return sortL[k-1]



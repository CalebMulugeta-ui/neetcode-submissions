# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, sort, k):
            #base case
            if not root:
                return
            

            left = dfs(root.left, sort,k)
            sort.append(root.val)
            if len(sort) == k:
                return sort
            right = dfs(root.right, sort,k)

            return sort
        
        sortL = []
        sortL = dfs(root, sortL,k)
        
        
        return sortL[k-1]



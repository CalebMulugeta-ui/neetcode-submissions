# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        posInf = float('inf')
        negInf = float('-inf')

        
        def dfs(root, low, high):
            if not root:
                return True

            #check if its within bounds
            if low < root.val and root.val < high:
                l = dfs(root.left, low, root.val) 
                r = dfs(root.right,root.val,high)
            else:
                return False

            if l and r:
                return True
            else:
                return False

        return dfs(root, negInf, posInf)

                
            


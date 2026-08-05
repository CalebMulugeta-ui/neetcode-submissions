# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def path(self,root,targetSum,num):
            if not root:
                return False

            num+= root.val

            if not root.left and not root.right:
                if num == targetSum:
                    return True
                else:
                    num -= root.val
                    return False

            if path(self,root.left,targetSum,num):
                return True
            if path(self,root.right,targetSum,num):
                return True

            return False 
            
        track = 0
        return path(self,root,targetSum,track)
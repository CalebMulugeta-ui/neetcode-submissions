# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #base case
        myList = []
        if not root:
            return myList 
        
        lList=self.inorderTraversal(root.left)
        myList.append(root.val)
        rList = self.inorderTraversal(root.right)
        final=lList + myList + rList
        
        return final
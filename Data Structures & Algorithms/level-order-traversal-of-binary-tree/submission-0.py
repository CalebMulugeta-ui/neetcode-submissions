# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        if root:
            queue.append(root)
        order = []
        while len(queue) > 0:
            inorder = []
            for i in range(len(queue)):
                inorder.append(queue[0].val)
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            order.append(inorder)
        return order



        

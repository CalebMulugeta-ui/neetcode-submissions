# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        if root:
            queue.append(root)
        else:
            return res

        while len(queue) > 0:
            res.append(queue[0].val)
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)

        return res

      
        
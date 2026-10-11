# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = [] #[[1],[2,3]]
        queue = deque() #[]

        if root:
            queue.append(root)
        else:
            return res


        while len(queue) > 0:
            tempL = [] #[2,3]

            for i in range(len(queue)):
                temp = queue.popleft()
                tempL.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            res.append(tempL)
                

        return res

      
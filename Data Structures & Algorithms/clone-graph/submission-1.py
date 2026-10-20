"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        mymap = {}
        queue = deque()
        queue.append(node)
        mymap[node] = Node(node.val)

        while queue:
            cur = queue.popleft()
            for n in cur.neighbors:
                if n not in mymap:
                    mymap[n] = Node(n.val)
                    queue.append(n)
                mymap[cur].neighbors.append(mymap[n])
            
        return mymap[node]







        

                        

        



        
        



        
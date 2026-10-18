from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #run regular bfs only difference is your directions
        #[[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        # down,up,right,left,down/right,down/left,up/right,up/left
        if grid[0][0] != 0:
            return -1


        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

        def bfs(r ,c):
            queue.append((r,c))
            visit.add((r,c))
            length = 1
            while queue:
                v = len(visit)
                for i in range(len(queue)):
                    currR, currC = queue.popleft()
                    if currR == ROWS - 1 and currC == COLS - 1:
                        return length

                    for dr, dc in directions:
                        r = currR + dr
                        c = currC + dc
                        if r in range(ROWS) and c in range(COLS) and grid[r][c] == 0 and (r,c) not in visit:
                            queue.append((r,c))
                            visit.add((r,c))
                            
                length += 1

            return -1

        return bfs(0,0)          




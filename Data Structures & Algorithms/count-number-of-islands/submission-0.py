from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        islands = 0

        def bfs(r,c):

            while queue:
                currR, currC = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    #check if its in range, if its a 1 and if its not visited
                    r = currR + dr
                    c = currC + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r, c) not in visit:
                        queue.append((r,c))
                        visit.add((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands+=1
                    queue.append((r,c))
                    visit.add((r,c))
                    bfs(r,c)
        
        return islands





           
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        #iterate thru every element, if its a 1 run bfs on it only if it hasnt been visisted, before that create a max island counter and start at 1, 
        #starat bfs
        #move in 4 directions and validate next islands if its valid add 1 to max islands, and mark it visited and add it to the queue


        ROW, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        maxIslands = 0

        def bfs(r,c,count):
            while queue:
                currR, currC = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r = currR + dr
                    c = currC + dc
                    if r in range(ROW) and c in range(COLS) and grid[r][c] == 1 and (r,c) not in visit:
                        queue.append((r,c))
                        visit.add((r,c))
                        count+=1

            return count


        for r in range(ROW):
            for c in range(COLS):
                count = 0
                if grid[r][c] == 1 and (r,c) not in visit:
                    count += 1
                    queue.append((r,c))
                    visit.add((r,c))
                    count = bfs(r,c,count)
                    if count > maxIslands:
                        maxIslands = count
        
        return maxIslands



        
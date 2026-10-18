from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #create fresh fruit set
        #iterate thru grid, if curr is fresh fruit add it to the freshFruit set
        #if curr is empty skip
        #if curr is rotten start bfs
        #at each iteration check valid paths, remove those fresh fruits from fresh fruit set and increase time by 1
        #keep going untill your queue is empty
        #after check if fresh fruit set is empty if it is return time else return -1

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        freshFruit = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruit+=1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0

        while queue and freshFruit > 0:
            for i in range(len(queue)):
                currR, currC = queue.popleft()
                for dr, dc in directions:
                    r = currR + dr
                    c = currC + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                        queue.append((r,c))
                        grid[r][c] = 2
                        freshFruit-=1
            time+=1
        

        if freshFruit == 0:
            return time
        else:
            return -1

        
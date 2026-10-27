from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        length = 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr,dc in neighbors:
                    if r+dr not in range(ROWS) or c+dc not in range(COLS) or (r+dr, c+dc) in visit or grid[r+dr][c+dc] == -1: 
                        continue
                    queue.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
                    grid[r+dr][c+dc] = length

            length+=1



        




        
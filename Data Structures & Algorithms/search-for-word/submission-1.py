class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROW, COLS = len(board), len(board[0])

        def dfs(r,c,visit,pointer):
            #check if its in bound
            if r not in range(ROW) or c not in range(COLS) or ((r,c) in visit):
                return False
            
            if board[r][c] != word[pointer]:
                return False

            if pointer == len(word)-1:
                return True
            
            visit.add((r,c))
            pointer+=1

            if dfs(r+1,c,visit,pointer) or dfs(r-1,c,visit,pointer) or dfs(r,c-1,visit,pointer) or dfs(r,c+1,visit,pointer):
                return True
            else:
                visit.remove((r,c))
                return False

        for r in range(ROW):
            for c in range(COLS):
                if dfs(r,c,set(),0):
                    return True

        return False





        
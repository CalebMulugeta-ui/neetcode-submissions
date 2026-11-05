class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squres = collections.defaultdict(set) #key = (r/3,c/3)


        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                #rows
                if board[r][c] in rows[r]:
                    return False
                else:
                    rows[r].add(board[r][c])
                
                #cols
                if board[r][c] in cols[c]:
                    return False
                else:
                    cols[c].add(board[r][c])
                
                #squres
                if board[r][c] in squres[(r//3,c//3)]:
                    return False
                else:
                    squres[(r//3,c//3)].add(board[r][c])
        

        return True

        
        
# https://leetcode.com/problems/surrounded-regions/
class Solution:
    # Time O(R*C)
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        # 1. O -> T capture unsorrundings
        def dfs(r,c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS - 1 or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
                

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O" and (r in [0,ROWS-1] or c in [0,COLS-1]):
                    dfs(r,c)    
        print(board)
        # 2. O -> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        print(board)            
        # 3. T -> O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

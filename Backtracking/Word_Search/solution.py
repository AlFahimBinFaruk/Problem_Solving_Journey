class Solution:
    # Time O(m*n*(4^w)) | Space O(H)
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we gonna use DFS backtracking approach to solve this.
        ROWS = len(board)
        COLS = len(board[0])
         
        # to dont visit the same row and column twice 
        visit = set()

        def dfs(r,c,i):
            # if we find the word
            if i == len(word):
                return True
            
            if  (r < 0 or 
                r >= ROWS or
                c < 0 or
                c >= COLS or 
                (word[i] not in board[r][c]) or 
                (r,c) in visit):
                return False


            # add the r,c we are now visiting
            visit.add((r,c))

            result = (dfs(r+1,c,i+1) or 
                      dfs(r-1,c,i+1) or 
                      dfs(r,c+1,i+1) or
                      dfs(r,c-1,i+1))

            # remove the r,c after visiting
            visit.remove((r,c))

            return result



        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False                

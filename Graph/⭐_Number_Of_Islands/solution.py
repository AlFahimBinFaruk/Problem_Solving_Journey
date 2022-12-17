class Solution:
    # Time O(ROWS * COLS) | Space O(ROWS * COLS)
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        isIsland = 0

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or grid[r][c] == "0"):
                return

            visit.add((r, c))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                # if it is land and not visited yet
                if grid[r][c] == "1" and ((r, c) not in visit):
                    isIsland += 1
                    # we will vist the land around it and add them also in visited.Because all those lands will create an Island
                    dfs(r, c)

        return isIsland

    
    ### BFS solution
    class Solution:
    # Time O(M * N) | Space O(N*M)
    def numIslands(self, grid: List[List[str]]) -> int:
        # we gonna use Breadth first search to solve this.
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        
        visit = set()
        isIsland = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                row , col = q.popleft()

                for dr , dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c)) 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)   
                    isIsland += 1     
        
        return isIsland
                       

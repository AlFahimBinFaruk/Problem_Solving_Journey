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

# https://leetcode.com/problems/island-perimeter/
class Solution:
    # Time O(N*M)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # we will go through every item if we found 1 we will not count it if we found 0 we will count it.
        visit = set()

        def dfs(r,c):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c]==0:
                return 1
            if (r,c) in visit:
                return 0

            visit.add((r,c))    

            perim = dfs(r,c+1)
            perim += dfs(r,c-1)
            perim += dfs(r+1,c)
            perim += dfs(r-1,c)

            return perim        

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(r,c)


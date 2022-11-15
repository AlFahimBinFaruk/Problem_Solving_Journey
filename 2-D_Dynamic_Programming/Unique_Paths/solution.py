class Solution:
    # Bottom-up solution.
    # Time O(N*M) | Space O(N)
    def uniquePaths(self, m: int, n: int) -> int:
        # m= top-to-bottom , n=left-to-right
        # bottom row and last-right row all value will be 1
        # bottom row
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                # newRow[j+1] = top-right value, row[j] = bottom
                newRow[j] = newRow[j+1] + row[j]
            row = newRow

        return row[0]

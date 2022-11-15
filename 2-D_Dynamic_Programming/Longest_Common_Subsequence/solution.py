class Solution:
    # Bottom-up approach
    # Time O(N*M) | Space O(N*M)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # i = Column, j = row
        dp = [[0 for j in range(len(text2) + 1)]
              for i in range(len(text1) + 1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                # if value matched we will set dp[i][j] to it's diagnal
                # if value don't match will set dp[i][j] to it's right and bottom value.
                if text1[i] == text2[j]:
                    # dp[i+1][j+1] will give us the diagnal of dp[i][j]
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]

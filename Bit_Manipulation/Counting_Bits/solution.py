class Solution:
    # Time O(N) | Space O(N)
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        # highest power of 2 is offset
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                # set new highest power of 2.
                offset = i
            dp[i] = 1 + dp[i-offset]

        return dp

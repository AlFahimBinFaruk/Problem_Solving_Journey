class Solution:
    # Time O(N) | Space O(N)
    def numDecodings(self, s: str) -> int:
        # handle out-of-bounds
        dp = { len(s): 1 }

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            # if i+1 is in bound and check for group value from 10-26
            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i + 2]


        return dp[0]                
    
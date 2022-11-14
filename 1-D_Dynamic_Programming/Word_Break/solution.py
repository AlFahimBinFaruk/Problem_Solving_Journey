class Solution:
    # Bottom-up solution
    # Time O(2^N) | Space O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        # Base case will always be true
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i+len(w)]
                # if the word is alrady matched
                if dp[i]:
                    break

        return dp[0]

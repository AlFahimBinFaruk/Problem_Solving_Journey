class Solution:
    # Bottom-up solution.
    # Time O(coins * len(amount)) | Space O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount + 1 is just a default value to monitor which we were unable to calculate.
        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a],dp[a-c]+1) # what we are saying is if a=7,b=4 dp[7] = 1+dp[3] could be a possible solution.

        return dp[amount] if dp[amount] != amount+1 else -1           

       
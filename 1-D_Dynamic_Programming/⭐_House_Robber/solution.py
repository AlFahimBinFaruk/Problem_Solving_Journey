class Solution:
    # Time O(N) | Space O(1)
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        # [rob1,rob2,n,n+1]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

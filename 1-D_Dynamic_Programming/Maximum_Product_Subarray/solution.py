class Solution:
    # Time O(N) | Space O(1)
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        currMax = 1
        currMin = 1

        for n in nums:
            tmpMax = currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * tmpMax, n * currMin, n)
            res = max(res, currMax)

        return res

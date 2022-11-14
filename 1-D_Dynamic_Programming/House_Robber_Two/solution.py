class Solution:
    # Time O(2n) | Space O(1)
    def rob(self, nums: List[int]) -> int:
        # nums[0] is for nums=[1]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    # helper
    def helper(self, myNums):
        rob1 = 0
        rob2 = 0

        for n in myNums:
            tmp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2

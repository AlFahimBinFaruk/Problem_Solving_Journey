class Solution:
    # Top-down approach
    # Time O(N^2) | Space O(N)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # default longest increasing subsq will be 1
        LIS = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                # check if it is in increasing order
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])


        return max(LIS)            
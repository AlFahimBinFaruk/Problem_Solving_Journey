# https://leetcode.com/problems/rotate-array/
class Solution:
    # Time O(nLogn)
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k > 0:
            l = 0
            r = len(nums) - 1
            while l < r:
                (nums[l],nums[r])=(nums[r],nums[l])
                l += 1
                r -= 1
            # handle first portion
            l = 0
            r = k - 1
            while l < r:
                (nums[l],nums[r])=(nums[r],nums[l])
                l += 1
                r -= 1   
            
            # handle second portion
            l = k
            r = len(nums)-1
            while l < r:
                (nums[l],nums[r])=(nums[r],nums[l])
                l += 1
                r -= 1   

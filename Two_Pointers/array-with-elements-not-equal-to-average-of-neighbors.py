# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
class Solution:
    # Time O(nlogn)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        
        result = []
        while len(result) != len(nums):
            result.append(nums[l])
            l += 1

            if l < r:
                result.append(nums[r])
                r -= 1

        return result   

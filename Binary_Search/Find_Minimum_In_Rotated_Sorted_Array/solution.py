# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    # Time O(logN)  | Space O(1)
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        result = float("infinity")

        while l <= r:
            # if the array is sorted
            if nums[l] < nums[r]:
                result = min(result,nums[l])
                # it makes the code more optimized.
                break
                

            mid = (l+r) // 2
            result = min(result,nums[mid])
            # if the array is part of left sorted portion 
            # we will search in right sorted portion
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                # or else we will search in the right sorted portion        
                r = mid - 1


        return result        

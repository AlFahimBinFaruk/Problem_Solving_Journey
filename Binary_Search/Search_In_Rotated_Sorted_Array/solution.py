# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    # Time O(logN) | Space O(1)
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search
        # as we will rotate the given sorted array ,there will be two sorted array(left sorted portion,right sorted portion.)
        l = 0
        r = len(nums) -1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                # Search in left sorted portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # search in right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1    

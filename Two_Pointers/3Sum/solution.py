# https://leetcode.com/problems/3sum/
class Solution:
    # Time O(N^2) | Space O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # in 3sum we will also use the logic of 2sum
        result = []
        # sort the input in assending order
        nums.sort()

        for i,n in enumerate(nums):
            # if the value is already checked
            if i > 0 and nums[i-1] == n:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:
                total = n + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -=1
                else:
                    result.append([n,nums[l],nums[r]])

                    l += 1
                    # if the value is alrady checked
                    while (l < r and nums[l] == nums[l-1]):
                        l += 1            

        return result    

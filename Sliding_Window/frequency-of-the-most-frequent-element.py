# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
class Solution:
    # Time O(n.logn)
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        l = 0
        r = 0
        
        result = 0
        while r < len(nums):
            total += nums[r]
            while (nums[r]*(r-l+1)) > (total+k):
                total -= nums[l]
                l += 1
            # does not work with all tests
            # if (nums[r]*(r-l+1)) <= (total+k):
            #     result = max(result,(r-l+1)) 
            result = max(result,(r-l+1))
            r += 1
        return result        

                

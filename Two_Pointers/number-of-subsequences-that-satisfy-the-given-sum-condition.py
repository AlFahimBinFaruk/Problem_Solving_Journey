# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
class Solution:
    # Time O(nLogn)
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort() # O(logn)
        mod = (10**9 + 7)
        result = 0

        r = len(nums) - 1
        for l,left in enumerate(nums):
            while (left + nums[r]) > target and l <= r:
                r -= 1

            if l <= r:
                result += 1<<(r - l)   
                # result += (2**(r-l))
                result %= mod    

        return result  

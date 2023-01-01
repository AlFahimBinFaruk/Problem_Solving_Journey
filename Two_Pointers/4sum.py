# https://leetcode.com/problems/4sum/
# Time O(N^2) | Space O(N)
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []

        def kSum(l,r,k,target,result,results):
            if r-l+1 < k or k < 2 or nums[l]*k > target or  nums[r]*k < target:
                return
            if k == 2:
                while l < r:
                    if (nums[l]+nums[r]) < target:
                        l += 1
                    elif (nums[l]+nums[r]) > target:
                        r -= 1
                    else:
                        results.append(result+[nums[l],nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
            else:
                for i in range(l,r+1):
                    if i == l or (i > l and nums[i] != nums[i-1]):
                        kSum(i+1,r,k-1,target-nums[i],result+[nums[i]],results)                        
                 

        kSum(0,len(nums)-1,4,target,[],results)    
        return results

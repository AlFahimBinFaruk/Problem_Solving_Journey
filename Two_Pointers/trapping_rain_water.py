# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    # Time O(N) | Space O(1)
    def trap(self, height: List[int]) -> int:
        # main formula = min(max(l),max(r)) - height[i]
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
    
        result = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax  = max(leftMax,height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax,height[r])
                result += rightMax - height[r]

        return result  

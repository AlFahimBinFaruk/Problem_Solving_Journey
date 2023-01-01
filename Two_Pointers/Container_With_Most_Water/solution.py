# https://leetcode.com/problems/container-with-most-water/
class Solution:
    # Time O(N) | Space O(1)
    def maxArea(self, height: List[int]) -> int:
        # two pointer - first , last
        # container = gap between two lines
        l = 0
        r = len(height) -1

        maxArea = 0

        while l < r:
            area = (r-l) * min(height[l],height[r])
            maxArea = max(maxArea,area)
            
            # we will always decrease the height that is smaller than another.
            if height[l] < height[r]:
                l += 1
            # elif height[l] > height[r]:
            #     r -= 1
            else:
                r -= 1

        return maxArea          

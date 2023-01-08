# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    # Time O(N) | Space O(N)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        deque = collections.deque()
        l = 0
        r = 0
        while r < len(nums):
            # we will add numbers in deque in decreasing order.
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)

            # when the window shifts
            if l > deque[0]:
                deque.popleft()

            # if the window is valid
            if (r-l+1) == k:
                result.append(nums[deque[0]])
                l += 1

            r += 1    

        return result 

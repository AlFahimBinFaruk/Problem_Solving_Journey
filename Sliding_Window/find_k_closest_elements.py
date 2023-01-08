# https://leetcode.com/problems/find-k-closest-elements/
class Solution:
    # Time O(logn+k)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # First step : we gonna use binary search to find the index of target x or number that is more close to x
        l = 0
        r = len(arr) - 1
        idx = 0 
        while l <= r:
            m = (l+r)//2
            currDiff = abs(arr[m] - x)
            resDiff = abs(arr[idx] - x)

            if currDiff < resDiff or (currDiff == resDiff and arr[m] < arr[idx]):
                idx = m

            if arr[m] > x:
                r = m - 1
            elif arr[m] < x:
                l = m + 1
            else:
                break
        
        # 2nd step : we gonna use that index to find its neighbours which will be our expected output
        l = r = idx
        for i in range(k-1):
            if l == 0:
                r += 1
            elif (r == len(arr)-1) or (x-arr[l-1] <= arr[r+1]-x):
                l -= 1 
            else:
                r += 1    
        return arr[l:r+1]                             

        

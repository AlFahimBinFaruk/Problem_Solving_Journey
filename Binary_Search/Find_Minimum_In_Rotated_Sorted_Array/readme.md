### Facebook interview question.

### Video Explanation
* [Neetcode](https://www.youtube.com/watch?v=nIVW4P8b1VA)

### Steps to solve
1. Initialize a variable call result with default value of first index of nums array.
   * result=nums[0]
2. Initialize left and right pointer:
   * l=0 
   * r=len(nums)-1
3. While l <= r :
   * mid = (l+r)//2
   * if the array is sorted means:
     * if nums[l] < nums[r]:
       * then result will be:
         * result = min(result,nums[l])        
   * update result value by comparing it with the current value of middle index:
     * result=min(result,nums[mid])
   * if current middle pointer value is greater of equal to the current left pointer value then increase l pointer value by mid + 1 :
     * if nums[mid] >= nums[l]:
       * l = mid + 1
     * else:
       * r = mid - 1
4. At the end of the iteration return the result which will be the expected output.
5. Time O(log(N)) | Space O(1).             
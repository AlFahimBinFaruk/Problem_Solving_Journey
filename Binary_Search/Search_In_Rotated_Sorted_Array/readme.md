### Google Interview Question.

### Vidoe Explanation
* [Neetcode](https://www.youtube.com/watch?v=U8XENwh8Oy8)

### Steps to solve:
1. Initialize left and right pointer with:
   * l = 0
   * r = len(nums) - 1
2. while l <= r : 
   * mid = (l+r) // 2   
   * if target == nums[mid]:
     * return mid **# Ultimately we will find the result in this block..**
   * Search left partition if :
     * if nums[l]<=nums[mid]:
       * if target > nums[mid] or target < nums[l]:
         * l = mid + 1
       * else:
         * r = mid - 1
   * Else search in right partition:
     * else:
       * if target < nums[mid] or target > nums[r]:
         * r = mid - 1
       * else:
         * l = mid + 1
3. If nothing is found return -1.
4. Time O(log(N)) | Space O(1)                     
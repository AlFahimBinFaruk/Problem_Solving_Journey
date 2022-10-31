### Video Explanation:
* [Neetcode](https://www.youtube.com/watch?v=KLlXCFG5TnA)

### Steps to solution : One pass
1. Initialize a hash-map call prevMap = {}
   * In this map key will be the number and value will be the index
2. iterate through every number in nums array:
   * for i,n in enumerate(nums):
     * diff=target-n(get the difference from target and current number which will give us the number we have to find in order to match the target):
       * if diff in prevMap(if we find the number):
         * return [prefMap[diff],i] = return the number index and current number index which **will be the result**.
       * then update the prevMap if it dosen't match:
         * prevMap[n]=i
3. By default return NULL if nothing matches. 
4. Time O(N) | Space O(N).      
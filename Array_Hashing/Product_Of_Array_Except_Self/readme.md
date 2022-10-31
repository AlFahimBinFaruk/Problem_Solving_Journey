### Explanation
* [Neetcode](https://www.youtube.com/watch?v=bNvIQI2wAjk)

### Steps to solve:
* We will use prefix and postfix to solve this.
1. Initialize a array call result with:
   * result = [1]*len(nums)
2. Prefix:
   * Default prefix will be 1.
   * Iteatare through nums array from start to end and for every iteration:
     * for i in range(len(nums)):
       * result[i] = prefix
       * prefix *=nums[i]
3. Postfix:
   * Default postfix will be  1.
   * Iterate through nums array from end to start and for every iteration:
     * for i in range(len(nums)-1,-1,-1):
       * result[i]*=postifx
       * postfix *=nums[i]

4. Return the result which will be our expected output.
5. Time O(N) | Space O(1).                   
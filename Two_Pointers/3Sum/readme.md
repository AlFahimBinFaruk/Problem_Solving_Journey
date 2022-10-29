### Vidoe Explanation
* [Neetcode](https://www.youtube.com/watch?v=jzZsG8n2R9A)

### Steps to Solve.
1. Sort the input(nums).
2. Iterate through every number inside nums array.
3. if i>0 and nums[i-1]==n then Continue(Don't do anything.)
4. Otherwise:
   * We will get 1st number of 3 sum which will be **n** .
   * Then initialize **left** and **right** pointer with 
    * l=i+1
    * r=len(i)-1
5. While l < r then we will get **threeSum** value for each : n+nums[l]+nums[r]
   * if the value is less than 0 : then we will increment l by one : l+=1
   * if the value is greater than 0 : then we will decrement r by one : r-=1
6. Otherwise(which means the value of threeSum is 0 which is our expected output) we will append this in result : [n,nums[l],nums[r]].
7. Then(we will start looking for other patters as there can be more patterns which addition will be 0)
   * we will increase l by one l+=1 
   * and if l < r and nums[l] == nums[l-1] (current item of nums[l] is not same as previous items of nums[l] which means nums[l-1].because we don't want any duplicate value one after another immediately) we will also increase l by one l+=1.
     * we can do the same steps for r instead of l but we only have to work with one (l or r) as in No:5 step we are handling it based on the increament we don't have to work on both l or r we can choose either one.
8. At last we will return result array which will have out expected output.
9. Time O(N ^ 2) | Space O(N)

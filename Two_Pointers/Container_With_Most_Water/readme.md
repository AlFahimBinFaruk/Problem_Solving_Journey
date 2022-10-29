### Explanation vidoe
* [Neetcode](https://www.youtube.com/watch?v=UuiTKBwPgAo)

### Solution Steps:
1. Initialize a variable name result with default value of 0.
2. Initialize left and right pointer with:
   * l = 0
   * r = len(height)-1
3. While l < r 
   * Calculate the area with = (r-l)*min(height[r],height[l])
     * r-l : width.
     * min(height[r],height[l]) :  height of the lowest point of container
   * Then set the result value each time for the highest area with :: result = max(area,result)
   * if height[l] < height[r] then increase left pointer value with l+=1
   * if height[r] < height[l] then decrease right pointer by one with r-=1
   * if above two condition don't match we will by default decrease right pointer by one with r-=1(we can remove the second if statement if we want beacause we are doing that anyway)
4. Then we will return the result after then end of iteration where we will find our output.
5. Time O(N) | Space(1)
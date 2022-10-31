### Solution Explanation:
* [Neetcode](https://www.youtube.com/watch?v=3OamzN90kPg)
* [The Conceptual](https://www.youtube.com/watch?v=Z_0nvQ7dGEc)

### Steps to solve:
1. Initialize a set called hashSet(as there can be no duplicate values in a set).
2. Iterate through every number in nums array and
   * if any number is already exits in the set and it has again occured:
     * return True as it is a duplicate
   * add every number we iterate through in the hashset.
3. If the loop has ended without returning True that means there is no duplicate so return False by default.
4. Time O(N) | Space O(N)     
### Video Explanation
* [Neetcode](https://www.youtube.com/watch?v=wiGpQwVHdE0)

### Steps to solve
1. create a set called CharSet(as we don't want any duplicate).
2. set default length to 0.
3. Initialize left pointer value with default 0
   * l= 0
4. Right pointer value will increase according to the length of given string
   * if we store given string in s variable.
   * for r in range(len(s)).
5. See if the current **right pointer** value is already present in the CharSet.
   * If it is already present:
      * increament **left pointer** by one :: l+=1.
      * and remove the current **left pointer** value from charecter set :: CharSet.remove(s[l]).
6. Then add the right pointer current value  to CharSet :: CharSet.add(s[r]).
7. Update the length with :: length = max(length,len(CharSet)).
8. Return the **length**.
9. Time O(N) | Space O(N).
### Explanation
* [Neetcode](https://www.youtube.com/watch?v=gqXU1UyA8pk)


* In here we will get only two types of character as input.Which means from 26 types(A-Z) we will get only two types of chareacters no matter what is the number.
* Example:
  * "AABABBA"
  * "ABAB"

### Steps to solve
1. Initialize a empty hash-map name charSet.
   * in hash-map we will store the character and their number of occurance 
   * example : {"A"->3,"B"->4}
2. Initialize maxLength and maxFreq with default 0.
3. Initialize left pointer value with 0.
4. Right pointer value will increase with the length of given string as argument (s).
5. See if the character already exits in the hash-map if exits update its value by 1 if don't exits then default value will be 1.
6. Update the maxFreq with:
   * max(maxFreq,char[s[r]]) : this will give us the max-frequency of a character in a sliding-window.
7. If we do :
   * WindowLen-maxFreq : this will give us the number of character we have to change to get our expected result.  
8. If our WindowLen-maxFreq > k(which is the number of type we can update a chareacter)
   * then we have to change the left pointer (and we have to do more updation operation than we can afford value of k).
   * we also have to decrease the chareacter value of the left pointer by one with charSet[s[l]]-=1 as we are not counting it anymore.
9. Then update maxLength with :: max(maxLength,r-l+1)
10. Return the maxLength which will be our expected result.
11. Time O(N) | Space O(N).  


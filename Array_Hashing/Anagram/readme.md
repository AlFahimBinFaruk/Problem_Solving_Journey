### Solution Explanation
* [Neetcode](https://www.youtube.com/watch?v=9UtInBqnCgA)
* [The Conceptual](https://www.youtube.com/watch?v=6BiyrT8yxaU)

### Steps to solve
* The main logic is to see if s input type has exactly the same character in same volume as input t.
1. Initialize two hash-map call 
   * counterS={}
   * counterT={}
2. iterate through every character of **s** input and :
   * counterS[s[i]] = counterS.get(s[i],0)+1
   * counterT[t[i]] = counterT.get(t[i],0)+1    
3. Then if each and every character and their volume in counterT match with counterS we will return true else we will return false.
4. Time O(S) | Space O(S+T)

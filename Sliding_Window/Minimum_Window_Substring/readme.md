### AirBnb Question.

### Vidoe Explanation 
* [Neetcode](https://www.youtube.com/watch?v=jSto0O4AJbM)


### Steps to solve.
1. Initialize two hash-map called countT = to count the occurance of character in **t** arg and window=to count the occurance of character in the current window of **s**
2. For every character in t:  
   * for c in t :
     * counT[c]=1+counT.get(c,0) :: we will initialize character as key and their number of occurance as value.
3. Initialize a variable call **have** with default value=0.
4. Initialize a variable call **need** with default value of length of countT.
5. Initialize a array call res with default value [-1,-1] with this we will monitor the left to right point of our sliding window where we will have our expected result.
6. Initialize a variable called resLength with default value of infinity (resLength = float("infinity")).
7. Initialize left pointer with l=0.
8. Iterate through every character in **s** and its index will be the value of right pointer **r**.
   * add every character in window hash-map
     *  window[c] = 1+window.get(c, 0)
   * if the chareacter is available is countT and it's value is excatly the number of value we need(if c in countT and countT[c] == window[c])
     * then increase have by one(have+=1).
   * while need == have :
     * if length of current window(r-l+1) is less than  resLength(if r-l+1 < resLength):
       * update resLength with r-l+1
       * update res value with res=[l,r]
   * Then as we have to move to the left we will remove the current character of left index from our window
     * window[s[l]]-=1
     * and if the character we have removed is available in countT and because of removing that if the number of that character we have declease from the number of that character we need then decrease have by one 
       * if s[l] in countT and window[s[l]] < countT[s[l]]:
         * have -= 1    
     * then increase the left pointer by one l+=1
9. Then if the maxLength is not Infinity then return the exprected with by slicing **s** with the values of res (l,r=res) otherwise return empty string "".
10. Time O(N+M) | Space O(N+M)   
### Solution Explanation
* [Neetcode](https://www.youtube.com/watch?v=vzdNOK2oB2E)

### Steps to solve : with Hash-map 
1. Initialize a empty dictionary call result with default value of empty list(the key of this dictionary will be tuple and values will be list).
2. Iterate through every string of given array of strings:
   * for every iteration initialize an array call count with 26 0 as default value(as there are 26 character in a-z)
     * [0]*26
     * In count array index number means the character and value means the number of occurance/volume the character has.
   * Iterate through every charater of current string:
     * get the index of that character with the help of ASCII value and each time increase it by one.
       * count[ord(char)-ord("a")]+=1(if char is a then index =0,if char is b then index = 1,if char is c then index=2)
   * Use the count to genarate a tuple.
     * use that tuple to get a key of result dictionary(if the key not exits it will create a key with default value of empty list) 
     * use that key to get the value of that item in the dictionary which will be a **list**.
     * append the current str on that list(in here we are mainly using the character of the string to genarate unique tuple reserve for only the same string pattern(if number of charater match)).    
3. Return the values of that result dictionary with will be the group of anagram.
4. Time O(N * M) | Space O(N * M).     
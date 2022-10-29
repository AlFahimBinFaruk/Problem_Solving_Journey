### Video Explanation
* [Neetcode](https://www.youtube.com/watch?v=jJXJ16kPFWg)


* Palindrome means if a string is readed the same in both forward and backward.
  * We will convert every character into lower-case for easy comparison.
  * Example : 
    * mom :: mom - Palindrome.
    * fahim :: mihaf - Not-Palindrome
            
### Steps to solve : Solution 01 : with build in methods
1. Initialize a variable called newStr="".
2. Iterate thourgh every character of input string.
3. Check if the character is **alpha-numeric(A-Z,a-z,0-9)** with built-in **isalnum()** method in python.
4. If it is alpha-numeric then append it to newStr with newStr+="e"
5. Then compare the newStr and the reverse version of newStr with each other and it will be the result.
6. Time O(N) | Space O(N)

### Steps to solve : Solution 02 : custom methods
1. Initialize left and right pointer with:
   * l=0
   * r=len(given str)-1
2. We need to write a custom function named alphaNum to see if the character is alpha-numeric:
   * s=the character we are checking.
   * (ord("A") <= ord(s) <= ord("Z") or ord("a") <= ord(s) <= ord("z") or ord("0") <= ord(s) <= ord("9")) :: given output will be true or false.
3. While l < r :
   * while l < r and left pointer value is not alpha-numeric (alphaNum(s[l])) we will increase left pointer by one : l+=1
   * while r > l and right pointer value is not alpha-numeric (alphaNum(s[r])) we will decrease right pointer by one : r-=1
4. Then we will compare both left ponter :: s[l] and right pointer :: s[r] (lower case version of them).If any character at pointer don't match we will return **false**. And the program will end
5. Otherwise we will return **true** by default.
6. Time O(N) | Space O(1)
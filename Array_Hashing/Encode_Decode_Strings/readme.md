### Explanation
* [Neetcode](https://www.youtube.com/watch?v=B1k_sxOSgv8)


### Steps to solve: Stiring Delimeter solution
* Encode the array of strings::
  1. Initialize a variable call result with empty string(result="").
  2. Iterate through every string of given array of strings and for every string add:
     * result +=str(len(s))+"#"+s = total length of s by converting it to string and a # and the string value s.
  3. Return the result which will be the encoded version.
  4. Time O(N) | Space O(1)
* Decode the Given string and return array::
  1. Initialize an empty array call result.
  2. Initialize a variable call i with default value 0.
  3. While i < len(given string):
     * j = i
     * while str[j] != "#" (current value of j index in str is not #):
       * j+=1
     * Find out the length of my current string that i want to add to the array with:
       * length = int(str[i:j])
     * Then append this string to result array with:
       * result.append(str[j+1:j+1+length])
     * Change the value of i pointer with the index of new string length with :
       * i = j+1+length
   4. Return the result will will be the decoded array of given string.
   5. Time O(N*K) | Space O(1).              
### Explanation
* [Neetcode](https://www.youtube.com/watch?v=P6RZZMu_maU)


### Steps to solve :
* Consequetive means it will go from small to big and each time the value will increase by 1 and a number cannot occur more than one.
1. Initialize a set call numSet with the values of nums(to remove duplicate).
2. Initialize a variable call longest with default value 0.
3. Iterate through every number in numSet
   * if the neighbour of that number(2 is the neighbour of ,3 neighbour of 4.Neighbour means 1 less that the current number) is available is numSet then we wont do anything as we have to star from the smallest number.
     * if it is not available then :
       * length = 1
       * while length+i (the next number of current number.next number of 4 is 5 , for 5 is 6) in numSet:
         * length+=1
       * update the value of longest = max length:
         * longest=max(longest,length)
4. Return the value of longest will will the length of longest consquetive sequence.
5. Time O(N) | Space O(N).            
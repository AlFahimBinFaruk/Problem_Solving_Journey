### Explanation
* [Neetcode](https://www.youtube.com/watch?v=YPTqKIgVk-k)

### Steps to solve: Bucket sort method
1. Initialize a hash-map call count.
2. Initialize a array call freq with :
   * freq=[[] for i in range(len(nums)+1)]
   * in freq array the index will be the number of occurance and their value will be the number.
3. Iterate though every number in nums array and add them to count dictionary with number as key and their occurance as value
   * for num in nums:
     * count[num] = 1+count.get(num, 0)   
4. Iterate through the items of count dictionary and add them to freq array as index as occurance and number as value
   * for key, val in count.items():
     * freq[val].append(key)   
5. Initialize a empty array call result=[]
6. Iterate thought the freq array from end to start(as we want the top most frequent occurance and in freq array occurance means index and we know that index are biggest to small in array end to start):
   * for i in range(len(freq)-1,-1,-1):
     * for j in freq[i](to see if freq[i] has a valid value or not as default value will be empty array which is not valid):
       *  result.append(j)
       * if (len(result)==k(the number of top occurance we can return)):
         * return result = which will be the expecter top frequent items array.
7. Time O(N^2)  |  Space O(N^2)         

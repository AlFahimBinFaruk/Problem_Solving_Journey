### Microsoft interview question.
* [Neetcode](https://www.youtube.com/watch?v=XIdigk956u0)

### Steps to solve:
1. Initialize a dummy-node to avoid the edge case of initial empty list.
   * dummy=ListNode()
   * the default value of tail will be the dummy node.
     * tail = dummy
2. While both list1 and list2 are valid:
   * while list1 and list2:
     * keep adding to tail depending on the condition. 
     * if list1.val < list2.val:
       * tail.next = list1
       * list1 = list1.next
     * else:
       * tail.next = list2
       * list2 = list2.next
     * tail = tail.next (always update the value of current tail)
3. Check if any of list1 or list2 is still iterable:
   * if list1:
     * tail.next = list1
   * if list2:
     * tail.next = list2
4. return dummy.next(in listnode the next has the values) where we will get the merged sorted list.
5. Time O(N+M) | Space O(N+M)                   
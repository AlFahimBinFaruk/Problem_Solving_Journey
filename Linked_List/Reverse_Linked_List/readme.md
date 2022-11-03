### Google and Facebook Question.
### Explanation:
* [Neetcode](https://www.youtube.com/watch?v=G0_I-ZF0S38)
### Steps to Solution : Iterative
* The solution will not work on code editors(you have to give linked list as an input) but it will work on LeetCode.
1. Initialize prev and curr with:
   * prev = none
   * curr = head
2. Until curr is not null:
   * while curr:
     * temp=curr.next(store the value of curr.next before changing it)
     * curr.next=prev
     * prev=curr
     * curr=temp   
   * main logic:
     * previous pointer to current pointer.
     * current pointer to current.next.  
3. Return the prev which will be the reversed linked-list.
4. Time O(N) | Space O(1) -> Most optimized solution.
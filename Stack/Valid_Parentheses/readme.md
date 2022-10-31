### Facebook Interview Question.

### Video Explanation

- [Neetcode](https://www.youtube.com/watch?v=WTzjTskDFMg)

### Steps to solve:

- The main logic is if the stack is empty that means the number of time items were appended are equal to the number of time they were deleted so we will return True else if the stack is not empty we will return False.

1. Initialize a stack name **stack** and a hash-map called **closeToOpen** with default value of:
   - closeToOpen = {")": "(", "}": "{", "]": "["}
   - stack = []
2. Iterate thourgh every item of given string s.
3. If an item is available in the **closeToOpen** hash-map then:
   - check if the value of that item is equal to the last item of stack which means stack[-1] == closeToOpen(current item):
     - pop the last item of the stack with stack.pop()
   - else return False.
4. Else append that item into the **stack**.
5. Return True if the length of the stack is 0 Else return False.
6. Time O(N) | Space O(N)

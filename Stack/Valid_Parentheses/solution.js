// https://leetcode.com/problems/valid-parentheses/
/**
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
*/

// Time O(N) | Space O(N)

const isValid = (s) => {
  let closeToOpen = new Map([
    [")", "("],
    ["}", "{"],
    ["]", "["],
  ]);
  let stack = [];

  for (let c of s) {
    if (closeToOpen.has(c)) {
      if (stack && stack[stack.length - 1] == closeToOpen.get(c)) {
        stack.pop();
      } else {
        return false;
      }
    } else {
      stack.push(c);
    }
  }
  if (stack.length == 0) {
    return true;
  } else {
    return false;
  }
};

console.log(isValid("()[]{}"));
console.log(isValid("(]"));

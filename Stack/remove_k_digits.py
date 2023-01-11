# https://leetcode.com/problems/remove-k-digits/
class Solution:
    # Time O(N) | Space O(N)
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k != 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        stack = stack[:len(stack)-k]    
        return str(int("".join(stack))) if stack else "0"   

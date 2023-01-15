# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    # Time O(N) | Space O(N)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop()+stack.pop())
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b-a))
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif tokens[i] == "*":
                stack.append(stack.pop()*stack.pop())
            else:
                stack.append(int(tokens[i]))       

        return stack[-1]                 

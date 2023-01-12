# https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                subStr = ""
                while stack and stack[-1] != "[":
                    subStr = stack.pop() + subStr
                # remove the [ 
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    # to handle double digits.
                    k = stack.pop() + k
                stack.append(int(k) * subStr)    
            else:
                stack.append(s[i])    

        return "".join(stack)       

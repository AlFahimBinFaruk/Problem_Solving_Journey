# https://leetcode.com/problems/simplify-path/
class Solution:
    # Time O(N) | Space O(N)
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            # empty string means / or //
            if p == "." or p == "":
                continue
            elif p == "..":
                if stack: stack.pop()
            else:
                stack.append(p)        
        return "/" + "/".join(stack)

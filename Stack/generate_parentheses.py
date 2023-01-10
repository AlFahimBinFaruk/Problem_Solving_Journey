# https://leetcode.com/problems/generate-parentheses/
class Solution:
    # Time O(2n)
    def generateParenthesis(self, n: int) -> List[str]:
        # add opening par if num of opening par < n
        # add closing par if num of closing par < Opening par
        # valid numOfclosing == numOfOpeing == n
        stack = []
        result = []

        def backtracking(openN,closingN):
            if openN == closingN == n:
                result.append("".join(stack))
                return 

            if openN < n:
                stack.append("(")
                backtracking(openN+1,closingN)
                stack.pop()   

            if closingN  < openN:
                stack.append(")")
                backtracking(openN,closingN+1)
                stack.pop()    

        backtracking(0,0)         
        return result 

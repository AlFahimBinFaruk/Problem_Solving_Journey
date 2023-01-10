# https://leetcode.com/problems/daily-temperatures/
# Time O(N^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        return result  

# Time O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:  
        result = [0] * len(temperatures)
        stack = [] # [index,temp]

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                popIn,popTemp = stack.pop()
                result[popIn] = i - popIn
            stack.append([i,t])

        return result 

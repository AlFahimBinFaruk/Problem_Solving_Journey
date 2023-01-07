# https://leetcode.com/problems/permutation-in-string/
class Solution:
    # O(s1​.log(s1​) + (s2​−s1​)s1​log(s1​)).
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = self.sortUtil(s1)
        
        for i in range(len(s2)):
            if s1 == self.sortUtil(s2[i:i+len(s1)]):
                return True
        return False        

    def sortUtil(self,s):
        newArr = list(s)
        newArr.sort() # O(n.logn)
        sortedStr = "".join(newArr)
        return sortedStr    

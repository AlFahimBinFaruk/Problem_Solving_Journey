# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    # Time O(S+T) | Space O(S+T)
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window
        if t == "":
            return ""

        # key = char,value = char occurance
        countT = {}
        countS = {}

        for c in range(len(t)):
            countT[t[c]] = 1 + countT.get(t[c],0)


        have = 0
        need = len(countT)

        res = [-1,-1]
        resLength = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c,0)

            if c in countT and countT[c] == countS[c]:
                have += 1   

            while need == have:
                if r-l+1 < resLength:
                    res = [l,r]
                    resLength = r-l+1

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1    


        l,r = res  
        return s[l:r+1] if resLength != float("infinity") else ""   

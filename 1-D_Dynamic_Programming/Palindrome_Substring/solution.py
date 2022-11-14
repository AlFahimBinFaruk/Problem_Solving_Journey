class Solution:
    # Time O(N^2) | Space O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # Odd Length
            l = i
            r = i
            res += self.countPalin(s,l,r)

            # Even
            l = i
            r = i+1
            res += self.countPalin(s,l,r)

        return res

    def countPalin(self,s,l,r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1        

        return res                 



        
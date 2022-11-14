class Solution:
    # Time O(N^2) | Space O(1)
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLength = 0
         
        # In this solution we have assume the current item as center and spread left,right from them to see if each of them are palindrome(same). 
        for i in range(len(s)):
            # Odd length
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLength:
                    res = s[l:r+1]
                    resLength = r-l+1
                l -= 1
                r += 1

            # Even Length
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLength:
                    res = s[l:r+1]
                    resLength = r-l+1
                l -= 1
                r += 1

        return res

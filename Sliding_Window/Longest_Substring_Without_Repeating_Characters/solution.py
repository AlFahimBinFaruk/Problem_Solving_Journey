# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    # Time O(N) | Space O(N)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        # the main trick here that the word cannot be repeated,order does not matter.
        charSet = set()
        l = 0
         
        maxLength = 0 
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])    
            maxLength = max(maxLength,len(charSet))

        return maxLength    


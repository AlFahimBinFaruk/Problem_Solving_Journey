# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    # Time O(N) | Space O(N)
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # In input type there will only be two types of characters(A,B or C,D)

        # key = string , value = string occurance
        charSet = {}
        # count the individual character max occurance in the length i have covered
        maxFreq = 0
        # monitor the max length     
        maxLength = 0

        l = 0

        for r in range(len(s)):
            charSet[s[r]] = 1 + charSet.get(s[r],0)
            maxFreq = max(maxFreq,charSet[s[r]])

            while (r-l+1) - maxFreq > k:
                charSet[s[l]] -= 1
                l += 1

            maxLength = max(maxLength,r-l+1)


        return maxLength   

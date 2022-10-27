# https://www.lintcode.com/problem/659/
"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode


Example1
Input: [“lint”,“code”,“love”,“you”] Output: [“lint”,“code”,“love”,“you”] Explanation: One possible encode method is: “4#lint4#code4#love3#you”

Example2
Input: [“we”, “say”, “:”, “yes”] Output: [“we”, “say”, “:”, “yes”]
"""

# String Delimiter

class Solution:
    # Encode Array of strings
    # Time O(N) | Space O(1)
    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s))+"#"+s

        return result

    # Decode String and return array
    # Time O(N * K) | Space O(N)
    def decode(self, str):
        result = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            result.append(str[j+1:j+1+length])
            i = j+1+length

        return result


test = Solution()
encoded = test.encode(["leet", "code"])
print("Encoded:", encoded)
print("Decoded:", test.decode(encoded))

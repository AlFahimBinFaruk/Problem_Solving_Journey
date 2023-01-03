# https://leetcode.com/problems/boats-to-save-people/
class Solution:
    # Time O(NlogN)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result = 0

        l = 0
        r = len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            result += 1

            if l <= r and people[l] <= remain:
                l += 1

        return result       

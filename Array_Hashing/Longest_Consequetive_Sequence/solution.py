# https://leetcode.com/problems/longest-consecutive-sequence/
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# time O(N) | space O(N)


def longestConsequetive(nums):
    numSet = set(nums)
    longest = 0

    for i in numSet:
        # see if i is the start sequence.
        if (i-1) not in numSet:
            length = 1
            # see if i has a next sequence
            while (i+length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


print(longestConsequetive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsequetive([100, 4, 200, 1, 3, 2]))
print(longestConsequetive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))

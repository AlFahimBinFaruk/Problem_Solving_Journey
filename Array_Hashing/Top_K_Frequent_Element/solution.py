# https://leetcode.com/problems/top-k-frequent-elements/
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

# Bucket sort method
# Time O(N^2) | Space O(N^2)

def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for num in nums:
        count[num] = 1+count.get(num, 0)

    for key, val in count.items():
        freq[val].append(key)

    result = []
    # -1 means decending order
    for i in range(len(freq)-1, -1, -1):
        for j in freq[i]:
            result.append(j)
            if (len(result) == k):
                return result


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([3,0,1,0], 1))
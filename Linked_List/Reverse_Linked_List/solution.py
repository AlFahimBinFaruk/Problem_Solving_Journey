# https://leetcode.com/problems/reverse-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Itereative Solution
# Time O(N) | Space O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            tempNxt = curr.next
            # this line is updating the pointer.
            curr.next = prev
            prev = curr
            curr = tempNxt

        return prev 

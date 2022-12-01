# https://leetcode.com/problems/merge-two-sorted-lists/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time O(N+M) | Space O(N+M)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # to avoid edge case of empty list
        dummy = ListNode()

        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        # handling another edge case
        if list1:
            head.next = list1

        if list2:
            head.next = list2

        return dummy.next      

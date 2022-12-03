# https://leetcode.com/problems/remove-nth-node-from-end-of-list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time O(N) | Space O(N)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we gonna use two pointers to solve this.
        dummy = ListNode(0,head)

        left = dummy
        right = head
        
        # shift right pointer depending on n
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete the expected node which will be at left.next
        left.next = left.next.next

        return dummy.next        

              


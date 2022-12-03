# https://leetcode.com/problems/reorder-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time O(N) | Space O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        ***
        the main concept is we will split the list in 1st and 2nd half.
        then we will keep changing the pointers by merging those list 1st half from starting to end , 2nd half from end to start.
        ***
        """
        # they want us to reorder in = 0th node -> last node -> 1st node -> 2nd last node -> 2nd node...
        # we gonna use slow,fast pointer to solve this.

        slow = head
        fast = head.next

        # find the middle of the list as we gonna split the list into two 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # determine the 2nd half of the list 
        secondList = slow.next
        # as slow.next will be the beginning of second list the first list slow.next will be null    
        slow.next = None

        # reverse the 2nd half(as we will traverse the 1st half from start to end and 2nd half from end to start).
        prev = None

        while secondList:
            tmpNxt = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = tmpNxt

        # merge two list    
        firstListNode = head
        secondListNode = prev

        while secondListNode:
            firstTmp = firstListNode.next
            secondTmp = secondListNode.next
            
            # updating the nodes.
            firstListNode.next = secondListNode
            secondListNode.next = firstTmp

            firstListNode = firstTmp
            secondListNode = secondTmp







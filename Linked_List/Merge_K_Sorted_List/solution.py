# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time O(N*Log(K)) | Space O(N)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
         
        # if length is 1 then the 0 indexed linked list is the answer. 
        while len(lists) > 1:
            mergedList = []

            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(self.mergeSortedList(l1,l2))
            
            lists = mergedList   
             
        return lists[0]       


    
    # Time O(N) | Space O(N)
    def mergeSortedList(self,l1,l2):
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

            head = head.next


        # handling edge case of if any of l1 or l2 remains empty
        if l1:
            head.next = l1

        if l2:
            head.next = l2

        return dummy.next                




    



# Time O(N) | Space O(N) 
# it sometimes exceed time limit
class SolutionTwo:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedList = None

        for i in range(len(lists)):
            mergedList = self.mergeTwoLists(mergedList, lists[i])

        return mergedList


def mergeTwoLists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next





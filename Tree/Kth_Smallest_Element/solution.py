# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(H+K) | Space O(H)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS Iteration - Preorder traversal
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val

            curr = curr.right       

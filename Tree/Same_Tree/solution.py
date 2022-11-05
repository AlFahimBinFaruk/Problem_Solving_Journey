# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(N+M) | Space O(1) - DFS-Recursion.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If the root is NULL
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            isSame = self.isSameTree(
                p.left, q.left) and self.isSameTree(p.right, q.right)
            return isSame
        else:
            return False

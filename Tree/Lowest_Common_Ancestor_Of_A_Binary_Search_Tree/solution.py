# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Time O(logN) | Space O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we gonna use DFS - iteration to solve this.
        current = root

        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                # if there is a split(if p and q are from different subtree)
                return current   

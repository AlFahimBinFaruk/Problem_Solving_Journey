# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS - recursion
    # Time O(N) | Space O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        return depth    
        

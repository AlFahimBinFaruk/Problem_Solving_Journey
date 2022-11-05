# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(N) | Space O(N) - Depth-first-search
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # in case of recursion checiking none case is very important other-wise it will be an infinite loop.
        # the recursion-algo will end when it will return None.
        if not root:
            return None

        # Swap the childs
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

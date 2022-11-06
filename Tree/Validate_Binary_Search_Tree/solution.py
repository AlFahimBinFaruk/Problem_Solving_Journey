# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(N) | Space O(H) H-the amount of space the recursion needs to execute
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, left, right):
            if not node:
                return True

            if not (node.val > left and node.val < right):
                return False

            return (isValid(node.left, left, node.val) and isValid(node.right, node.val, right))

        return isValid(root, float("-inf"), float("inf"))
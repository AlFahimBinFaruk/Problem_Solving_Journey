# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(N*M) | Space O(1)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is null wheather subTree of root is null or not it will always return true
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            isSame = self.sameTree(root.left, subRoot.left) and self.sameTree(
                root.right, subRoot.right)
            return isSame
        else:
            return False

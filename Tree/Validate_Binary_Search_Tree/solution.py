# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(N) | Space O(N)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validTree(root,float("-inf"),float("inf"))
    
    def validTree(self,root,left,right):
        # DFS - recursion
        # if we get a null root we will return true,because technically an empty binary search tree is still a valid binary search tree.
        if not root:
            return True
        
        # see if they match binary search tree conditions.
        if not (left < root.val and right > root.val):
            return False
        
        # the left and right subtree mush also be valid b-s-t 
        # while checking left subtree we will always keep the left -inf
        # while checking right subtree we will always keep the right inf
        return (self.validTree(root.left,left,root.val) and self.validTree(root.right,root.val,right))  

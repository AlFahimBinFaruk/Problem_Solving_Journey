# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(N) | Space O(N)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we gonna use DFS - recursion to solve this.

        # if both roots are null then it is a same tree.
        if not p and not q:
            return True

        if (p and q) and (p.val == q.val):
            # if root/parent nodes are same then we will check the left,right nodes.
            isSame = (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))  
            return isSame
        else:
            return False      
        
               

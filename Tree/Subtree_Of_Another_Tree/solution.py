# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(N*M) | Space O(N+M)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS - recursion
        
        # if there is not subroot (subroot is Null) then it will always return True because we then have to look for null in root and we are sure that there will be a null in root.
        if not subRoot:
            return True

        # if subroot is not null but root is null then we will return False becoz we have no root to match subroot.
        if not root:
            return False


        # see if the structure of root and subRoot match.if match return True from there and end the algo.
        if self.sameTree(root,subRoot):
            return True   
        
        # then search in both left and right subtree to see if the subRoot matches.
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))         



    
    # Time O(N) | Space O(N)
    def sameTree(self,p,q):
        if not p and not q:
            return True

        if (p and q) and (p.val == q.val):
            isSame = (self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right))
            return isSame
        else:
            return False            
                 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(N) | Space O(N)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Interting means swapping child of each nodes
        # we gonna use DFS(recursion) to solve this.
         
        if not root:
            return None

        # swapping the child nodes
        tmpLeft = root.left
        root.left = root.right
        root.right =  tmpLeft

        # moving to next nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        

        

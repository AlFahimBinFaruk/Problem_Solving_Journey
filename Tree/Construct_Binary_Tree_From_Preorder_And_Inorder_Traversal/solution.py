# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Time O(N^2) | Space O(N)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # DFS - recursion
        # we have to return the binray tree in preorder
        if not preorder or not inorder:
            return None
         
        # create root node 
        root = TreeNode(preorder[0])

        # find the value of that preorder[0] in inorder
        mid =  inorder.index(preorder[0])
        
        # Defines tree left and right nodes
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root

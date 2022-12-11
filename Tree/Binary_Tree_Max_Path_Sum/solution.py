# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(N) | Space O(H)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS - recursion
        # we have to monitor max path of every recursion.
        # we will update res depending on every recursion call if the max path value is 
        # higher than before as path does not need to pass through the root. 
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            # if we get any negative values we will not include them as including childrens is optional.
            leftSum = max(dfs(root.left),0)
            rightSum = max(dfs(root.right),0)
            
            # update res by splitting the tree
            res[0] = max(res[0],(root.val+leftSum+rightSum))

            # return response without splitting the tree
            return (root.val + max(leftSum,rightSum))

        dfs(root)

        return res[0]     

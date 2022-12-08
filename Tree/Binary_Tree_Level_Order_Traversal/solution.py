# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(N) | Space O(N)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS - iteration
        # main concept is that at first we will keep the items of a level in deque,when we finished traversing that deque we will remove it from deque.
        result = []

        # deque DS to monitor level we are traversing.
        q = collections.deque()

        if root:
            q.append(root)
        
        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                
                # check if the node has left,right child.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(val)


        return result                
        
          

        

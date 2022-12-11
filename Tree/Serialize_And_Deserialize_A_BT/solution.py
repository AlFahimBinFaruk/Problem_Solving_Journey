# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Time O(N) | Space O(H) 
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res  = []

        # DFS - recursion
        def dfs(root):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return ",".join(res)        

           
        
    # Time O(N) | Space (H)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data =  data.split(",")
        self.i = 0

        # DFS - recursion
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None

            newNode = TreeNode(int(data[self.i]))
            self.i += 1

            newNode.left = dfs()
            newNode.right = dfs() 

            return newNode

        return dfs()       

        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

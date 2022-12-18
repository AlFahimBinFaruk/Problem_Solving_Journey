class Solution:
    # Time O(N+E) | Space O(N+E)
    def validTree(self, n, edges):
        if not n:
            return True

        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        # to make sure there is no loop
        def dfs(i, prevNode):
            if i in visited:
                return False

            visited.add(i)

            for j in adj[i]:
                if j == prevNode:
                    continue
                if not dfs(j, i):
                    return False

            return True
        # it is a valid tree if there is no loop and all the nodes are connected(n=len(visited))
        return (dfs(0, -1) and n == len(visited))

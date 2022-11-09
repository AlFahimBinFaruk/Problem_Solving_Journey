# Time O(E * a(N)) | Space O(V)
class UnionFind:
    def __init__(self):
        # key = child, value = parent
        self.f = {}

    def findParent(self, x):
        y = self.f.get(x, x)

        if x != y:
            y = self.f[x] = self.findParent(y)

        return y

    def union(self, x, y):
        self.f[self.findParent[x]] = self.findParent[y]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ufa = UnionFind()

        for a, b in edges:
            ufa.union(a, b)

        result = len(set(ufa.findParent(i) for i in range(n)))
        return result

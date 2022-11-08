class Solution:
    # Time O(N+P) -N=numCoursese,P=prerequisites
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we will use the number of courses we can take to make the prerequisites map
        # in preMap key=course and value is [course prerequisites]
        preMap = {i: [] for i in range(numCourses)}

        for cr, pr in prerequisites:
            preMap[cr].append(pr)

        visited = set()

        def dfs(cr):
            if cr in visited:
                return False
            if preMap[cr] == []:
                return True

            visited.add(cr)

            for pr in preMap[cr]:
                if not dfs(pr):
                    return False

            visited.remove(cr)
            preMap[cr] = []
            return True

        for cr in range(numCourses):
            if not dfs(cr):
                return False

        return True

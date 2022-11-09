from typing import (
    List,
)


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        if not words:
            return ""

        if len(set(words)) == 1:
            return "".join(set(c for c in words[0]))

        adj = {char: set() for word in words for char in word}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLength = min(len(w1), len(w2))
            # check if word order is invalid
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""

            for j in range(minLength):
                if w1[j] != w2[j]:
                    # which means w1 comes before w2
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # False = Visited , True = Current Path
        res = []

        # if it returns True which means there is an loop so it's an invalid order so we will return ""
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for nei in adj[char]:
                if dfs(nei):
                    return True

            visited[char] = False
            res.append(char)

        for char in sorted(adj.keys(), reverse=True):
            if dfs(char):
                return ""
        # as we are using post-order-DFS we have to reverse res before returning.
        res.reverse()
        return "".join(res)

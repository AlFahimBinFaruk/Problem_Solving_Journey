class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.maxWordLength = 0

    # Time O(N) | Space O(N)
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
        self.maxWordLength = max(self.maxWordLength, len(word))

    # Time O(N) | Space O(N)
    def search(self, word: str) -> bool:
        # In order to prevent searching a word that length is greater than any word i have store so we can immediately return False in order for optimization.
        if len(word) > self.maxWordLength:
            return False

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if (dfs(i+1, child)):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.endOfWord

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

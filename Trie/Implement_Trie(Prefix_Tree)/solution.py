# main trie node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
"""
Structure of this will be ->  {a={p={p={l={e}}}}}
"""
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    # Time O(N) | Space O(1)
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            # if the character dont exists we will add it
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # then we will move to it to find its childs.    
            curr = curr.children[c] 

        curr.endOfWord = True       

        
    # Time O(N) | Space O(1)
    def search(self, word: str) -> bool:
        # we have to make sure that every char in available in node
        # and it is an complete word.
        curr = self.root

        for c in word:
            # if character is not in node then we will return false
            if c not in curr.children:
                return False    
            curr = curr.children[c]     
        
        return curr.endOfWord
 

    # Time O(N) | Space O(1)
    def startsWith(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]    
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

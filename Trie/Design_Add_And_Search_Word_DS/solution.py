# We gonna use Trie DS to solve this
class TrieNode:
    def __init__(self):
        # key = node , val = child
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.maxWordLength = 0
        
    
    # Time O(N) | Space O(1)
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True 
        # we will always keep track which is the biggest word in our trie to optimized the code
        self.maxWordLength = max(self.maxWordLength,len(word))       
        
    
    # Time O(N) | Space O(1)
    def search(self, word: str) -> bool:

        if len(word) > self.maxWordLength:
            return False

        def dfs(j,root):
            curr = root

            for i in range(j,len(word)):
                c = word[i]
                
                # if the char is . then we have to match every child of that node to make sure its valid or not
                if c == ".":
                    for child in curr.children.values():
                        if (dfs(i+1,child)):
                            return True
                    # only after we have matched every child and didnt find any pattern we will return false.        
                    return False    
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]   

            return curr.endOfWord  

        return dfs(0,self.root)                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

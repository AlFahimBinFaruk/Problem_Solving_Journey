class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
        self.refs=0

    # Time O(N) | Space O(N)
    def addWord(self,word):
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr = curr.children[c]
            curr.refs +=1
        curr.endOfWord = True

    # Time O(N) | Space O(N)
    def removeWord(self,word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1                

class Solution:
    # Time O((ROWS * COLS) * (4 * (3 ^ (WORDS - 1)))) | Space O(N)
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)

        ROWS = len(board)
        COLS = len(board[0])

        res = set()
        visit = set()


        def dfs(r,c,node,word):
            if (r not in range(ROWS) or 
            c not in range(COLS) or 
            board[r][c] not in node.children or 
            node.children[board[r][c]].refs < 1 or 
            (r,c) in visit):
                return    


            visit.add((r,c))

            node = node.children[board[r][c]]

            word += board[r][c]

            if node.endOfWord:
                node.endOfWord = False
                res.add(word)
                root.removeWord(word)



            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)  
            dfs(r,c+1,node,word) 
            dfs(r,c-1,node,word) 

            visit.remove((r,c))    


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")


        return list(res)            
        
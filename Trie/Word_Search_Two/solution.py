# we gonna use Trie node to do this
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        # to optimize code
        self.refs = 0

    # adding words
    def addWord(self,word):
        curr = self
        curr.refs += 1   
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # then we will shift to its child    
            curr = curr.children[c]
            # and update it refs
            curr.refs += 1   
        curr.endOfWord = True

    # remove word - we will remove a word when we will find it
    def removeWord(self,word):
        curr = self
        curr.refs -= 1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs -= 1     



class Solution:
    # Time O(ROWS*COLS*(4^longestLengthOfString)) | Space O(N)
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])
        
        # output cannot contains duplicate words.
        result  = set()
        # here we will monitor the current node we are visiting   
        visit = set()

        # we are going to use DFS to find the words in Trie
        def dfs(r,c,node,word):
            # handling edge cases
            if (r not in range(ROWS) or 
            c not in range(COLS) or 
            (board[r][c] not in node.children) or 
            (node.children[board[r][c]].refs < 1) or 
            ((r,c) in visit)):
                return
            
            # add it to visit as we are currently visiting it
            visit.add((r,c))

            # as the word exits we will shift the node to its child
            node = node.children[board[r][c]]
            # and add to word to word string
            word += board[r][c]    

            if node.endOfWord:
                # as we find the word we will add it to the result
                result.add(word)
                # if we find the word we will remove it from trie to optimze the code
                node.endOfWord = False
                # then we will remove the word from root
                root.removeWord(word)
             
            # call dfs for top,bottom,left,right from each node 
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            # after visiting the [r][c] we will remove it from visit
            visit.remove((r,c))
        
        # iterate through every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(result)               

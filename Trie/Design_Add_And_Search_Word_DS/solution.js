class TrieNode {
  constructor() {
    this.children = {};
    this.endOfWord = false;
  }
}

class WordDictionary {
  constructor() {
    this.root = new TrieNode();
  }

  // Time O(N) | Space O(N)
  addWord(word) {
    let curr = this.root;

    for (let c of word) {
      if (!curr.children[c]) {
        curr.children[c] = new TrieNode();
      }
      curr = curr.children[c];
    }

    curr.endOfWord = true;
  }

  // Time O(N) | Space O(N)
  search(word) {
    var dfs = function (j, root) {
      let curr = root;

      for (let i = j; i < word.length; i++) {
        let c = word[i];
        if (c == ".") {
          for (let child of Object.values(curr.children)) {
            if (dfs(i + 1, child)) {
              return true;
            }
          }
          return false;
        } else {
          if (!curr.children[c]) {
            return false;
          }

          curr = curr.children[c];
        }
      }

      return curr.endOfWord;
    };

    return dfs(0, this.root);
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

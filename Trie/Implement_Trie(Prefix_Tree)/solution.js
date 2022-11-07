class TrieNode {
  constructor() {
    this.children = {};
    this.endOfWord = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }
  // Time O(N) | Space O(N)
  insert(word) {
    let curr = this.root;

    for (let c of word) {
      if (!curr.children[c]) {
        curr.children[c] = new TrieNode();
      }

      curr = curr.children[c];
    }
    curr.endOfWord = true;
  }

  // Time O(N) | Space O(1)
  search(word) {
    let curr = this.root;

    for (let c of word) {
      if (!curr.children[c]) {
        return false;
      }
      curr = curr.children[c];
    }
    return curr.endOfWord;
  }

  // Time O(N) | Space O(1)
  startsWith(prefix) {
    let curr = this.root;

    for (let c of prefix) {
      if (!curr.children[c]) {
        return false;
      }
      curr = curr.children[c];
    }

    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */

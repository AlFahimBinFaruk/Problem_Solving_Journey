class TrieNode {
  constructor() {
    this.children = {};
    this.endOfWord = false;
    this.refs = 0;
  }

  // Time O(N) | Space O(N)
  addWord(word) {
    let curr = this;
    curr.refs += 1;
    for (let c of word) {
      if (!curr.children[c]) {
        curr.children[c] = new TrieNode();
      }
      curr = curr.children[c];
      curr.refs += 1;
    }

    curr.endOfWord = true;
  }

  // Time O(N) | Space O(N)
  removeWord(word) {
    let curr = this;
    curr.refs -= 1;

    for (let c of word) {
      if (curr.children[c]) {
        curr = curr.children[c];
        curr.refs -= 1;
      }
    }
  }
}


// Time O((ROWS * COLS) * (4 * (3 ^ (WORDS - 1)))) | Space O(N)
/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function (board, words) {
  let root = new TrieNode();

  for (let w of words) {
    root.addWord(w);
  }

  let ROWS = board.length;
  let COLS = board[0].length;

  let res = new Set();
  let visit = new Set();

  var dfs = function (r, c, node, word) {
    if (
      r < 0 ||
      ROWS <= r ||
      c < 0 ||
      COLS <= c ||
      visit.has(`(${r},${c})`) ||
      !node.children[board[r][c]] ||
      node.children[board[r][c]].refs < 1
    ) {
      return;
    }

    visit.add(`(${r},${c})`);

    node = node.children[board[r][c]];

    word += board[r][c];

    if (node.endOfWord) {
      node.endOfWord = false;
      res.add(word);
      root.removeWord(word);
    }

    dfs(r + 1, c, node, word);
    dfs(r - 1, c, node, word);
    dfs(r, c + 1, node, word);
    dfs(r, c - 1, node, word);

    visit.delete(`(${r},${c})`);
  };

  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      dfs(r, c, root, "");
    }
  }

  return [...res];
};

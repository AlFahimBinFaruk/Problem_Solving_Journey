// Time O(N*M*(4^n) | Space O(H)
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  let ROWS = board.length;
  let COLS = board[0].length;

  let visit = new Set();

  var dfs = function (r, c, i) {
    if (i == word.length) {
      return true;
    }

    if (
      r < 0 ||
      c < 0 ||
      r >= ROWS ||
      c >= COLS ||
      word[i] != board[r][c] ||
      visit.has(`(${r},${c})`)
    ) {
      return false;
    }

    visit.add(`(${r},${c})`);

    let res =
      dfs(r + 1, c, i + 1) ||
      dfs(r - 1, c, i + 1) ||
      dfs(r, c + 1, i + 1) ||
      dfs(r, c - 1, i + 1);

    visit.delete(`(${r},${c})`);

    return res;
  };

  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      if (dfs(r, c, 0)) {
        return true;
      }
    }
  }

  return false;
};

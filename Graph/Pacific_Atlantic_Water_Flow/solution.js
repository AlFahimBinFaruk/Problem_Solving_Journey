// Time O(ROWS * COLS) | Space O(ROWS * COLS)
/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function (heights) {
  let ROWS = heights.length;
  let COLS = heights[0].length;

  let pac = new Set();
  let atl = new Set();

  var dfs = function (r, c, visit, prevHeight) {
    if (
      visit.has(`(${r},${c})`) ||
      r < 0 ||
      c < 0 ||
      r >= ROWS ||
      c >= COLS ||
      heights[r][c] < prevHeight
    ) {
      return;
    }

    visit.add(`(${r},${c})`);
    dfs(r + 1, c, visit, heights[r][c]);
    dfs(r - 1, c, visit, heights[r][c]);
    dfs(r, c + 1, visit, heights[r][c]);
    dfs(r, c - 1, visit, heights[r][c]);
  };

  for (let c = 0; c < COLS; c++) {
    dfs(0, c, pac, heights[0][c]);
    dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]);
  }

  for (let r = 0; r < ROWS; r++) {
    dfs(r, 0, pac, heights[r][0]);
    dfs(r, COLS - 1, atl, heights[r][COLS - 1]);
  }

  let res = [];

  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      if (pac.has(`(${r},${c})`) && atl.has(`(${r},${c})`)) {
        res.push([r, c]);
      }
    }
  }

  return res;
};

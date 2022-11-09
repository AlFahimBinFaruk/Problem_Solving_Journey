// Time O(N+E) | Space O(N+E)
export class Solution {
  /**
   * @param n: An integer
   * @param edges: a list of undirected edges
   * @return: true if it's a valid tree, or false
   */
  validTree(n, edges) {
    if (!n) {
      return true;
    }

    let adj = new Map();
    for (let i = 0; i < n; i++) {
      adj.set(i, []);
    }

    for (let i = 0; i < edges.length; i++) {
      let n1 = edges[i][0];
      let n2 = edges[i][1];
      let arrOne = adj.get(n1);
      arrOne.push(n2);
      adj.set(n1, arrOne);

      let arrTwo = adj.get(n2);
      arrTwo.push(n1);
      adj.set(n2, arrTwo);
    }

    let visited = new Set();
    function dfs(i, prevNode) {
      if (visited.has(i)) {
        return false;
      }

      visited.add(i);

      let ajdArr = adj.get(i);
      for (let j of ajdArr) {
        if (j == prevNode) {
          continue;
        }
        if (!dfs(j, i)) {
          return false;
        }
      }

      return true;
    }

    if (dfs(0, -1) && n == visited.size) {
      return true;
    } else {
      return false;
    }
  }
}

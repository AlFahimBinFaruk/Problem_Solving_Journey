/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */

// Time O(N+P) -N=numCoursese,P=prerequisites
var canFinish = function (numCourses, prerequisites) {
  let preMap = new Map();
  for (let i = 0; i < numCourses; i++) {
    preMap.set(i, []);
  }

  for (let i = 0; i < prerequisites.length; i++) {
    cr = prerequisites[i][0];
    pr = prerequisites[i][1];
    let arr = preMap.get(cr);
    arr.push(pr);
    preMap.set(cr, arr);
  }

  let visited = new Set();

  var dfs = function (cr) {
    if (visited.has(cr)) {
      return false;
    }
    if (preMap.get(cr) == []) {
      return true;
    }

    visited.add(cr);

    for (let pr of preMap.get(cr)) {
      if (!dfs(pr)) {
        return false;
      }
    }
    visited.delete(cr);
    preMap.set(cr, []);
    return true;
  };

  for (let i = 0; i < numCourses; i++) {
    if (!dfs(i)) {
      return false;
    }
  }

  return true;
};

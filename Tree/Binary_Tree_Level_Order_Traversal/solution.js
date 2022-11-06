/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// Time O(N) | Space O(N)
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  let result = [];
  // This will work as a queue(some method have to be implemented differently as it is not a pure queue like python queue.)
  let q = [];

  if (root) {
    q.push(root);
  }

  while (q.length) {
    let val = [];
    // Negative Iteration.
    for (let i = q.length - 1; 0 <= i; i--) {
      let node = q.shift(); //removes the first left elm
      val.push(node.val);
      if (node.left) {
        q.push(node.left);
      }
      if (node.right) {
        q.push(node.right);
      }
    }
    result.push(val);
  }

  return result;
};

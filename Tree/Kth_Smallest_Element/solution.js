/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// Time O(N+K) | Space O(H)
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  let stack = [];
  let n = 0;
  let curr = root;

  while (curr || stack) {
    while (curr) {
      stack.push(curr);
      curr = curr.left;
    }

    curr = stack.pop();
    n += 1;
    if (n == k) {
      return curr.val;
    }
    curr = curr.right;
  }
};

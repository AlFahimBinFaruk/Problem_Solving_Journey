/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// Time O(N) | Space O(H)
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function (root) {
  let res = root.val;

  var dfs = function (root) {
    if (!root) {
      return 0;
    }

    let leftMax = dfs(root.left);
    let rightMax = dfs(root.right);
    leftMax = Math.max(leftMax, 0);
    rightMax = Math.max(rightMax, 0);

    // calculate the res with split
    res = Math.max(res, root.val + leftMax + rightMax);

    // return the max value without split
    return root.val + Math.max(leftMax, rightMax);
  };

  dfs(root);

  return res;
};

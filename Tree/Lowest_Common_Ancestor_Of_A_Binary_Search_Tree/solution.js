/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

// Time O(log(N)) | Space O(1)
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  let current = root;
  while (current) {
    if (p.val > current.val && q.val > current.val) {
      current = current.right;
    } else if (p.val < current.val && q.val < current.val) {
      current = current.left;
    } else {
      return current;
    }
  }
};

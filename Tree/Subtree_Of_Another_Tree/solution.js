/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

// Time O(N*M) | Space O(1)
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  // If subRoot is null wheather subTree of root is null or not it will always return true
  if (!subRoot) {
    return true;
  }

  if (!root) {
    return false;
  }

  if (sameTree(root, subRoot)) {
    return true;
  }

  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

var sameTree = function (r, s) {
  if (!r && !s) {
    return true;
  }

  if (r && s && r.val == s.val) {
    isSame = sameTree(r.left, s.left) && sameTree(r.right, s.right);
    return isSame;
  } else {
    return false;
  }
};

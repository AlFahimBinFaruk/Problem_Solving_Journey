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
 * @return {boolean}
 */
var isValidBST = function (root) {
  var isValid = function (node, left, right) {
    // practically if node is empty then it is an valid binary-tree
    if (!node) {
      return true;
    }
    if (!(node.val > left && node.val < right)) {
      return false;
    }
    //left , right means -Infinity and Infinity
    return (
      isValid(node.left, left, node.val) && isValid(node.right, node.val, right)
    );
  };

  return isValid(root, parseFloat(-Infinity), parseFloat(Infinity));
};

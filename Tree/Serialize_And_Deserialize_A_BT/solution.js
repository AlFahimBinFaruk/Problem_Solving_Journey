/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

// Time O(N) | Space O(H)
/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function (root) {
  let result = [];

  var dfs = function (node) {
    if (!node) {
      result.push("N");
      return;
    }
    result.push(node.val.toString());
    dfs(node.left);
    dfs(node.right);
  };
  console.log(result.join(","));
  dfs(root);
  return result.join(",");
};

// Time O(N) | Space O(H)
/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
  let vals = data.split(",");
  let i = 0;

  var dfs = function () {
    if (vals[i] == "N") {
      i += 1;
      return null;
    }
    let node = new TreeNode(parseInt(vals[i]));
    i += 1;
    node.left = dfs();
    node.right = dfs();

    return node;
  };

  return dfs();
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */

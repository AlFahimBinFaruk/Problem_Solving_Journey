/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */


// Time O(N*C) | Space O(C)
/**
 * @param {Node} node
 * @return {Node}
 */
 var cloneGraph = function(node) {
    let oldToNew=new Map()

    var dfs=function(node){
        if(oldToNew.get(node)){
            return oldToNew.get(node)
        }

        let copy =new Node(node.val)
        oldToNew.set(node,copy)

        for(let nei of node.neighbors){
            copy.neighbors.push(dfs(nei))
        }
        return copy

    }
    
    if(node){
        return dfs(node)
    }else{
        return null
    }
};
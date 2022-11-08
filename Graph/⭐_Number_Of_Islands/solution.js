// Time O(ROWS * COLS) | Space O(ROWS * COLS)
/**
 * @param {character[][]} grid
 * @return {number}
 */
 var numIslands = function(grid) {
    if(!grid || (!grid[0])){
        return 0
    }

    let isIsland=0
    let visit = new Set()

    let ROWS = grid.length
    let COLS = grid[0].length

    var dfs=function(r,c){
        if((r<0)||(r>=ROWS) || (c<0) || (c>=COLS) || grid[r][c]=="0" || (visit.has(`(${r},${c})`))){
            return 
        }

        visit.add(`(${r},${c})`)

        let directions=[[0,1],[0,-1],[1,0],[-1,0]]

        for(let i of directions){
            dr=i[0]
            dc=i[1]

            dfs(r+dr,c+dc)
        }
    }

    for(let r=0; r<ROWS; r++){
        for(let c=0; c<COLS; c++){
            if(grid[r][c]=="1" && (!visit.has(`(${r},${c})`))){
                isIsland+=1
                dfs(r,c)
            }
        }
    }

    return isIsland
    
};
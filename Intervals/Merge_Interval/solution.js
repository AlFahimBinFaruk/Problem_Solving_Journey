// Time O(N*LogN) | Space O(N)
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function(intervals) {
    intervals.sort(([aStart, aEnd], [bStart, bEnd]) =>
        aStart !== bStart ? aStart - bStart : aEnd - bEnd
    );

    let res = [intervals[0]]

    for(let i=1;i<intervals.length;i++){
        let start=intervals[i][0]
        let end=intervals[i][1]

        let lastEnd=res[res.length-1][1]

        if(start<=lastEnd){
            res[res.length-1][1]=Math.max(lastEnd,end)
        }else{
            res.push([start,end])
        }
    }

    return res
    
};
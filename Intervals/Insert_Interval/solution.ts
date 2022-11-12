// Time O(N) | Space O(N)
function insert(intervals: number[][], newInterval: number[]): number[][] {
  let res: any = [];

  for (let i = 0; i < intervals.length; i++) {
    if (newInterval[1] < intervals[i][0]) {
      res.push(newInterval);
      let after = intervals.slice(i);
      return [...res, ...after];
    } else if (newInterval[0] > intervals[i][1]) {
      res.push(intervals[i]);
    } else {
      newInterval = [
        Math.min(intervals[i][0], newInterval[0]),
        Math.max(intervals[i][1], newInterval[1]),
      ];
    }
  }

  res.push(newInterval);
  return res;
}

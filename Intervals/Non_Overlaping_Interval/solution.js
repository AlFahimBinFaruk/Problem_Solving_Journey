// Time O(N*LogN) | Space O(1)
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  intervals.sort(([aStart, aEnd], [bStart, bEnd]) =>
    aStart !== bStart ? aStart - bStart : aEnd - bEnd
  );

  let prevEnd = intervals[0][1];
  let res = 0;
  for (let i = 1; i < intervals.length; i++) {
    let start = intervals[i][0];
    let end = intervals[i][1];
    // does not over-lap
    if (start >= prevEnd) {
      prevEnd = end;
    } else {
      res += 1;
      prevEnd = Math.min(end, prevEnd);
    }
  }

  return res;
};

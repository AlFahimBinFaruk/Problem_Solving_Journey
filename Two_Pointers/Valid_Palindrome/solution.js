/**
 * 2 Pointer | Midde Convergence
 * Time O(N) | Space O(1)
 * @param {string} s
 * @return {boolean}
 */
const isPalindromeSolutionOne = (s) => {
  if (!s.length) return false;

  let l = 0;
  let r = s.length - 1;
  while (l < r) {
    while (l < r && !alphaNum(s[l])) {
      l += 1;
    }
    while (r > l && !alphaNum(s[r])) {
      r -= 1;
    }

    if (s[l].toLowerCase() != s[r].toLowerCase()) {
      return false;
    }
    l += 1;
    r -= 1;
  }
  return true;
};

const alphaNum = (c) => {
  let code = c.toLowerCase().charCodeAt(0);

  const [a, z] = [97, 122];
  const isAlpha = a <= code && code <= z;

  const [zero, nine] = [47, 57];
  const isNumeric = zero <= code && code <= nine;

  return isAlpha || isNumeric;
};

console.log(isPalindromeSolutionOne("A man, a plan, a canal: Panama"));
console.log(isPalindromeSolutionOne("race a car"));


/**
 * Array - Filter && Clone && Reverse
 * Time O(N) | Space O(N)
 * @param {string} s
 * @return {boolean}
 */
 var isPalindromeSolutionTwo = function(s) {
    if (!s.length) return true;
    
    const alphaNumeric = filterAlphaNumeric(s);/* Time O(N) | Space O(N) */
    const reversed = reverse(alphaNumeric);    /* Time O(N) | Space O(N) */
    
    return alphaNumeric === reversed;
};

const filterAlphaNumeric = (s, nonAlphaNumeric = new RegExp('[^a-z0-9]','gi')) => s
    .toLowerCase()               /* Time O(N) | Space O(N) */
    .replace(nonAlphaNumeric, '')/* Time O(N) | Space O(N) */

const reverse = (s) => s
    .split('')/* Time O(N) | Space O(N) */
    .reverse()/* Time O(N) | Space O(N) */
    .join('');/* Time O(N) | Space O(N) */
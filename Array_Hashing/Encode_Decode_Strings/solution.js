// https://www.lintcode.com/problem/659/
/**
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings. Please implement encode and decode


Example1
Input: [“lint”,“code”,“love”,“you”] Output: [“lint”,“code”,“love”,“you”] Explanation: One possible encode method is: “4#lint4#code4#love3#you”

Example2
Input: [“we”, “say”, “:”, “yes”] Output: [“we”, “say”, “:”, “yes”]
*/

// Solution 01:  String Delimiter

class SolutionOne {
  // Encode
  // Time O(N) | Space O(1)
  encode(strs) {
    let result = "";

    for (let s of strs) {
      result += s.length + "#" + s;
    }

    return result;
  }

  // Decode
  // Time O(N*K) | Space O(N)
  decode(str) {
    let result = [];
    let i = 0;

    while (i < str.length) {
      let j = i;
      while (str[j] !== "#") {
        j += 1;
      }
      let length = parseInt(str.slice(i, j));
      result.push(str.slice(j + 1, j + 1 + length));
      i = j + 1 + length;
    }

    return result;
  }
}

let test = new SolutionOne();
let encode = test.encode(["we", "say", ":", "yes"]);
console.log("Encoded", encode);
console.log("Decoded", test.decode(encode));


//  Solution 02:  Non-ASCII Delimiter - Ignore Auxiliary Space

class SolutionTwo{
    // Time O(N) | Space O(1)
    encode(strs){
        let nonASCIICode=String.fromCharCode(257)
        return strs.join(nonASCIICode)
    }
    
    // Time O(N) | Space O(1)
    decode(str){
        let nonASCIICode=String.fromCharCode(257)
        return str.split(nonASCIICode)
    }
}

let testTwo = new SolutionTwo();
let encodeTwo = testTwo.encode(["we", "say", ":", "yes"]);
console.log("Encoded", encodeTwo);
console.log("Decoded",testTwo.decode(encodeTwo))
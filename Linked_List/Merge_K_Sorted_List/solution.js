// ***********************************************
// Solution One : More Efficient in Practical - Time O(N*log(K)) | Space O(N+K)
// **************************************************
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  if (!lists || lists.length == 0) {
    return null;
  }

  while (lists.length > 1) {
    let mergedList = [];

    for (let i = 0; i < lists.length; i += 2) {
      let l1 = lists[i];
      let l2 = null;
      if (i + 1 < lists.length) {
        l2 = lists[i + 1];
      }

      mergedList.push(mergeList(l1, l2));
    }

    lists = mergedList;
  }

  return lists[0];
};

var mergeList = function (l1, l2) {
  let dummy = new ListNode();
  let tail = dummy;
  while (l1 && l2) {
    if (l1.val < l2.val) {
      tail.next = l1;
      l1 = l1.next;
    } else {
      tail.next = l2;
      l2 = l2.next;
    }
    tail = tail.next;
  }

  if (l1) {
    tail.next = l1;
  }
  if (l2) {
    tail.next = l2;
  }

  return dummy.next;
};

// *************************************
// Solution Two:Less efficent in practical - Time O(N) | Space O(N)
// *******************************************

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

// Time O(N) | Space O(N)

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  let mergedList = null;

  for (let i = 0; i < lists.length; i++) {
    mergedList = mergeTwoList(mergedList, lists[i]);
  }

  return mergedList;
};

var mergeTwoList = function (l1, l2) {
  let dummy = new ListNode();
  let tail = dummy;
  while (l1 && l2) {
    if (l1.val < l2.val) {
      tail.next = l1;
      l1 = l1.next;
    } else {
      tail.next = l2;
      l2 = l2.next;
    }
    tail = tail.next;
  }

  if (l1) {
    tail.next = l1;
  }
  if (l2) {
    tail.next = l2;
  }

  return dummy.next;
};

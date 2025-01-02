"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""

from utils.linked_list import Node, linked_list_from_list, list_from_linked_list
from typing import Optional
import math

tests = [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], []),
]


def mergeKLists(lists: list[Optional[Node]]) -> Optional[Node]:
    """
    Idea: Use minimum of all lists
    Time: O(n*k)?
    Memo: O(1)
    Better: store heads in a priority queue or join two lists iteratively util all joined
    """
    head = Node(0)
    tail = head

    # remove empty lists
    # e.g. [[],[1,2]]
    lists = [l for l in lists if l]

    while lists:
        # select minimum
        min_node = Node(math.inf)
        min_idx = math.inf
        for idx, node in enumerate(lists):
            if node.val < min_node.val:
                min_node = node
                min_idx = idx
        tail.next = min_node
        tail = tail.next

        # create new list
        lists_new = []
        for idx, node in enumerate(lists):
            if idx == min_idx:
                if node.next:
                    lists_new.append(node.next)
                continue
            lists_new.append(node)
        lists = lists_new
    return head.next


if __name__ == "__main__":
    for idx, (lists, exp) in enumerate(tests):
        print(idx)
        print(lists)
        lists = [linked_list_from_list(l) for l in lists]
        act = mergeKLists(lists)
        act = list_from_linked_list(act)
        print(act, exp)
        assert act == exp
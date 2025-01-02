from __future__ import annotations
"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head (first node) of the merged linked list.

Example 1: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2: list1 = [], list2 = []
Output: []

Example 3: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    next: Node


def merge_two_lists(node1: Optional[Node], node2: Optional[Node]) -> Node:
    """
        Time: O(n) where n = min(len(l1), len(l2))
        Memo: O(1)

        Can also be done without head pointer
    """
    head = Node(0, None)
    tail = head
    while node1 and node2:
        if node1.val <= node2.val:
            head.next = node1
            node1 = node1.next
        else:
            head.next = node2
            node2 = node2.next
        head = head.next
    if node1:
        head.next = node1
    if node2:
        head.next = node2
    return tail.next
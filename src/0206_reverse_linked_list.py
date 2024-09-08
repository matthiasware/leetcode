from __future__ import annotations
"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1: head = [1,2,3,4,5] Output: [5,4,3,2,1]
Example 2: head = [1,2] Output: [2,1]
Example 3: head = [] Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or
recursively. Could you implement both?
"""

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: Node


tests = [
    (None, None),
    (
        Node(1, (Node(2, Node(3, Node(4, Node(5, None)))))),
        Node(5, Node(3, Node(2, Node(1, None)))),
    ),
]


def print_linked_list(node: Node) -> None:
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)


def reverse_list(head: Node | None) -> Node:
    """
        Time: O(n)
        Memo: O(1)
    """
    prior = None
    current = head
    while current:
        next = current.next

        # reverse
        current.next = prior

        prior = current
        current = next
    return prior


if __name__ == "__main__":
    for node, exp in tests:
        print(node)
        act = reverse_list(node)
        print(act)

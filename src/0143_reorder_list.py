"""
143. Reorder Linked List

You are given the head of a singly linked-list.
The positions of a linked list of length = 7
for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n
the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes,
but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""
from utils.linked_list import (
    Node, list_from_linked_list,
    linked_list_from_list
)
from collections import namedtuple

Test = namedtuple("Test", ("list", "exp"))

tests = [
    Test([1], [1]),
    Test([1, 2], [1, 2]),
    Test([1, 2, 3], [1, 3, 2]),
    Test([1, 2, 3, 4], [1, 4, 2, 3]),
    Test([0, 1, 2, 3, 4, 5, 6], [0, 6, 1, 5, 2, 4, 3]),
    Test([2, 4, 6, 8], [2, 8, 4, 6]),
    Test([2, 4, 6, 8, 10], [2, 10, 4, 8, 6]),
]


def reorder_list(head: Node) -> Node:
    """
    Time: O(n)
    Memo: O(1)
    """
    # find length of list
    node = head
    length = 0
    while node:
        length += 1
        node = node.next
    
    # move node to middle
    node = head
    for _ in range(length // 2):
        node = node.next

    # reverse starting from middle
    prior = None
    while node:
        next = node.next
        node.next = prior
        prior = node
        node = next

    # merge
    tik = head
    tok = prior
    dummy = Node(0)
    tail = dummy
    for _ in range(length//2):
        tail.next = tik
        tik = tik.next
        tail = tail.next

        tail.next = tok
        tail = tail.next
        tok = tok.next

    if tok:
        tail.next = tok
    head = dummy.next


if __name__ == "__main__":
    for lst, exp in tests:
        node = linked_list_from_list(lst)
        # inplace
        reorder_list(node)
        act = list_from_linked_list(node)
        print(act, exp)
        assert act == exp
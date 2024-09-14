"""
19. Remove Node From End of Linked List

You are given the beginning of a linked list head, and an integer n.
Remove the nth node from the end of the list and return the beginning of the list.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 2
Output: [2]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

from utils.linked_list import (
    Node, list_from_linked_list,
    linked_list_from_list
)
from collections import namedtuple

Test = namedtuple("Test", ("lst", "n", "exp"))
tests = [
    Test([1, 2], 1, [1]),
    Test([1, 2, 3, 4], 2, [1, 2, 4]),
    Test([5], 1, []),
    Test([1, 2], 2, [2])
]


def remove_from_end(head: Node, n: int) -> Node:
    """
        Time: O(n)
        Memo: O(1)
    """
    # 1) get length of ll
    node = head
    length = 0
    while node:
        length += 1
        node = node.next
    
    # 2) create new list with pointers:
    # - dummy: beginning of new list
    # - tail: end of new list 
    dummy = Node(0)
    tail = dummy

    # add all elements before n-th to new list
    node = head
    for _ in range(length - n):
        tail.next = node
        tail = node
        node = node.next
    # add remaining elements to new list
    if (length - n) <= length - 2:
        tail.next = node.next
    else:
        tail.next = None

    return dummy.next


def remove_from_end_distance(head: Node, n: int) -> Node:
    """
        Time: O(n)
        Memo: O(1)
    """
    res = Node(0, head)
    dummy = res

    for _ in range(n):
        head = head.next

    while head:
        dummy = dummy.next
        head = head.next

    dummy.next = dummy.next.next
    return res.next


if __name__ == "__main__":
    for lst, n, exp in tests:
        head = linked_list_from_list(lst)
        head = remove_from_end_distance(head, n)
        act = list_from_linked_list(head)
        print(n, lst, act, exp)

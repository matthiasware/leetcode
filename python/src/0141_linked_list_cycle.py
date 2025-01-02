"""
141. Linked List Cycle
Easy

Topics
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""

from utils.linked_list import Node
from typing import Optional
from collections import namedtuple


Test = namedtuple("Test", ("node", "exp"))


def get_test1() -> Node:
    n1 = Node(3)
    n2 = Node(2)
    n3 = Node(0)
    n4 = Node(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    return n1, True


def get_test2() -> Node:
    n1 = Node(1)
    n2 = Node(2)
    n1.next, n2.next = n2, n1
    return n1, True


def get_test3() -> Node:
    n1 = Node(1)
    n2 = Node(2)
    n1.next, n2.next = n2, None
    return n1, False


tests = [
    Test(Node(1), False),
    Test(*get_test1()),
    Test(*get_test2()),
    Test(*get_test3()),
]


def has_cycle_attr(head: Optional[Node]) -> bool:
    """
        Time: O(n)
        Memo: O(n)
    """
    node = head
    while node:
        if hasattr(node, 'visited'):
            return True
        node.visited = True
        node = node.next
    return False


def has_cycle_set(head: Optional[Node]) -> bool:
    """
        Time: O(n)
        Memo: O(n)
    """
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False


def has_cycle_constraints(head: Optional[Node]) -> bool:
    """
        Time: O(?)
        Memo: O(1)
    """
    n_visited = 0
    while head:
        head = head.next
        n_visited += 1
        if n_visited > 10**4:
            return True
    return False


def has_cycle_floyd(head: Optional[Node]) -> bool:
    """
        Time: O(n)
        Memo: O(1)
    """
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False


if __name__ == "__main__":
    for node, exp in tests:
        act = has_cycle_floyd(node)
        print(node, exp, act)

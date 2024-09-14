"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

from collections import namedtuple
from utils.linked_list import linked_list_from_list, list_from_linked_list, Node

Test = namedtuple("Test", ("lst1", "lst2", "exp"))
tests = (
    Test([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    Test([0], [0], [0]),
    Test([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
)


def add_two_numbers_1(h1: Node, h2: Node) -> Node:
    dummy = Node(0)
    cur = dummy
    carry_flag = 0
    while h1 and h2:
        list_sum = h1.val + h2.val + carry_flag
        carry_flag, val = divmod(list_sum, 10)
        node = Node(val)
        cur.next = node
        cur = cur.next
        h1 = h1.next
        h2 = h2.next
    h = h1 if h2 is None else h2
    while h:
        list_sum = h.val + carry_flag
        carry_flag, val = divmod(list_sum, 10)
        node = Node(val)
        cur.next = node
        cur = cur.next
        h = h.next
    if carry_flag:
        cur.next = Node(carry_flag)
    return dummy.next


def add_two_numbers_2(h1: Node, h2: Node) -> Node:
    dummy = Node(0)
    cur = dummy
    carry_flag = 0
    while h1 or h2:
        list_sum = carry_flag
        if h1:
            list_sum += h1.val
            h1 = h1.next
        if h2:
            list_sum += h2.val
            h2 = h2.next
        carry_flag, val = divmod(list_sum, 10)
        cur.next = Node(val)
        cur = cur.next
    if carry_flag:
        cur.next = Node(carry_flag)
    return dummy.next


def add_two_numbers(h1: Node, h2: Node) -> Node:
    dummy = Node(0)
    cur = dummy
    carry = 0
    while h1 or h2 or carry:
        list_sum = carry
        v1 = h1.val if h1 else 0
        v2 = h2.val if h2 else 0

        list_sum = v1 + v2 + carry

        carry, val = divmod(list_sum, 10)
        cur.next = Node(val)

        h1 = h1.next if h1 else None
        h2 = h2.next if h2 else None
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    for lst1, lst2, exp in tests:
        head1 = linked_list_from_list(lst1)
        head2 = linked_list_from_list(lst2)
        head_act = add_two_numbers(head1, head2)
        act = list_from_linked_list(head_act)
        print("act", act)
        print("exp", exp)
        assert act == exp
        print("*" * 100)

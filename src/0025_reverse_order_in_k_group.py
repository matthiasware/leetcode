"""
25. Reverse Nodes in k-Group

Given the head of a linked list,
reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k
then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes,
only nodes themselves may be changed.

 

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

from typing import Optional
from collections import namedtuple
from utils.linked_list import Node, linked_list_from_list, list_from_linked_list

Test = namedtuple("Test", ["list", "k", "exp"])

tests = [
    ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 6, 5, 4, 7]),
]


def reverseKGroup(head: Optional[Node], k: int) -> Optional[Node]:
    """
        Time: O(n)
        Memo: O(1)
        Idea: Check if group is big enough
        if so reverse that group and add it to new list
        otherwise add rest of list to new list.
    """
    head_new = Node(0)   # head of new list
    tail_new = head_new  # always points to tail of new list
    tail = head          # will point to tail of subgroup

    while True:
        # move tail k-1 forward
        n = 1
        while tail and n < k:
            tail = tail.next
            n += 1

        # if group is too small, tail is None
        # so add the rest of the list to new list
        if not tail:
            tail_new.next = head
            break
        
        # reset pointers
        tail_new.next = tail
        tail_new = head
        tail = tail.next

        # reverse everything from head to tail
        prior = None
        current = head
        while current != tail:
            next = current.next

            current.next = prior

            prior = current
            current = next

        # reset head
        head = tail
    return head_new.next


if __name__ == "__main__":
    for lst, k, exp in tests:
        head = linked_list_from_list(lst)
        act = reverseKGroup(head, k)
        act = list_from_linked_list(act)
        print(lst, exp, act)
        assert act == exp

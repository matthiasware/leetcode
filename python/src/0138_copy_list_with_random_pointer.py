"""
138. Copy List with Random Pointer

A linked list of length n is given such that each node
contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list.
The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value
of its corresponding original node.
Both the next and random pointer of the new nodes
should point to new nodes in the copied list
such that the pointers in the original list and copied list
represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list,
where X.random --> Y, then for the corresponding two nodes x and y in the copied list,
x.random --> y.

Return the head of the copied linked list.
The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 
Example 1:
Input: head = [[7,null]->[13,0]->[11,4]->[10,2->[1,0]]
Output:       [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output:       [[7,null],[13,],[11,],[10,],[1,]]

Example 2:
Input: head = [[1,1],[2,1]]
Output:       [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output:       [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list
"""

from __future__ import annotations

tests = (
    [[1, None]],
    [[1, 0]],
    [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
    [[1, 1], [2, 1]],
    [[3, None], [3, 0], [3, None]],
)


class Node:
    def __init__(
        self, x: int, next: Node = None, random: Node = None, idx=None
    ) -> None:
        self.val = x
        self.next = next
        self.random = random
        self.idx = idx

    def __repr__(self) -> str:
        if self.idx is not None:
            next = None
            if self.next:
                next = self.next.idx
            random = None
            if self.random:
                random = self.random.idx
            return f"{self.__class__.__name__}({self.val}, {next}, {random})"
        return f"{self.__class__.__name__}({self.val}, {self.next})"


def ll_from_list(lst: list[(int, int)]) -> Node:
    dummy = Node(0)
    idx_to_nodes = {}
    tail = dummy
    for idx, (val, _) in enumerate(lst):
        node = Node(val, idx=idx)
        idx_to_nodes[idx] = node
        tail.next = node
        tail = tail.next

    tail = dummy.next
    for _, idx in lst:
        if idx is not None:
            tail.random = idx_to_nodes[idx]
        tail = tail.next

    return dummy.next


def ppll(head: Node):
    res = []
    while head:
        res.append(
            [
                head.val,
                head.next.idx if head.next is not None else None,
                head.random.idx if head.random is not None else None,
            ]
        )
        head = head.next
    res = "->".join(f"N({val},{next},{random})" for val, next, random in res)
    print(res)


def list_from_ll(head: Node) -> list[(int, int)]:
    res = []
    node_to_idx = {}
    idx = 0
    node = head
    while node:
        node_to_idx[node] = idx
        idx += 1
        node = node.next
    node = head
    idx = 0
    while node:
        random = None
        if node.random:
            random = node_to_idx[node.random]
        res.append([node.val, random])
        idx += 1
        node = node.next
    return res


def copy_random_list_first_try(head: Node) -> Node:
    # maps nodes to its copies
    node_to_copy = {}

    tail_orig = head

    # copy list without random pointer
    dummy = Node(0)
    tail_copy = dummy
    while tail_orig:
        node = Node(tail_orig.val, idx=tail_orig.idx)
        tail_copy.next = node
        tail_copy = node

        node_to_copy[tail_orig] = tail_copy
        tail_orig = tail_orig.next

    # add random pointer
    tail_copy = dummy.next
    tail_orig = head

    while tail_orig:
        if tail_orig.random is not None:
            tail_copy.random = node_to_copy[tail_orig.random]
        tail_copy = tail_copy.next
        tail_orig = tail_orig.next
    return dummy.next


def copy_random_list(head: Node) -> Node:
    # maps nodes to its copies
    node_to_copy = {None: None}

    # copy nodes and put in map
    cur = head
    while cur:
        copy = Node(cur.val)
        node_to_copy[cur] = copy
        cur = cur.next

    # set pointers for copies
    cur = head
    while cur:
        copy = node_to_copy[cur]
        copy.next = node_to_copy[cur.next]
        copy.random = node_to_copy[cur.random]
        cur = cur.next
    return node_to_copy[head]


if __name__ == "__main__":
    for lst in tests:
        head = ll_from_list(lst)
        copy = copy_random_list(head)
        ppll(head)
        lst_out = list_from_ll(copy)
        assert lst == lst_out
        print("*" * 100)

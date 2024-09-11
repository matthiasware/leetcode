from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, val: Any, next: Node = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.val},{self.next is not None})"


def printll(node: Node):
    lst = list_from_linked_list(node)
    print(lst)


def list_from_linked_list(node: Node) -> list[int]:
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals


def linked_list_from_list(lst: list[int]) -> Node:
    tail = Node(0, None)
    head = tail
    for val in lst:
        head.next = Node(val, None)
        head = head.next
    return tail.next


if __name__ == "__main__":
    lst = [1, 0, 3]
    node = linked_list_from_list(lst)
    printll(node)

    a = Node(1)
    b = a
    print(a == b, a is b)
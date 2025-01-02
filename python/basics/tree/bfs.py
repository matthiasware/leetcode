from collections import deque
from tree import get_trees, print_tree, Node
from typing import Any


def breath_first_search(node: Node) -> list[Any]:
    deq = deque()
    deq.appendleft(node)
    trav_data = []
    while deq:
        node = deq.pop()
        trav_data.append(node.data)
        if node.left:
            deq.appendleft(node.left)
        if node.right:
            deq.appendleft(node.right)
    return trav_data


if __name__ == "__main__":
    for tree in get_trees():
        print_tree(tree)
        trav_data = breath_first_search(tree)
        print(trav_data)

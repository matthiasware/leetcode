from tree import get_trees, print_tree, Node
from typing import Any


def depth_first_search(node: Node) -> list[Any]:
    stack = []
    stack.append(node)
    trav_data = []
    while stack:
        node = stack.pop()
        trav_data.append(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return trav_data


def depth_first_search_rec(node: Node, trav_data: Any = None) -> list[Any]:
    if not trav_data:
        trav_data = []
    if not node:
        return
    trav_data.append(node.data)
    depth_first_search_rec(node.left, trav_data)
    depth_first_search_rec(node.right, trav_data)
    return trav_data


if __name__ == "__main__":
    for tree in get_trees():
        print_tree(tree)
        trav_data = depth_first_search_rec(tree)
        print(trav_data)

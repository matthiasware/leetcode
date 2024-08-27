from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    left: Optional['Node'] = None
    right: Optional['Node'] = None


_trees = [
    # one node
    {
        'data': 0
    },
    # three nodes
    {
        'data': 0,
        'left':
        {
            'data': 1
        },
        "right":
        {
            'data': 2
        }
    },
    # two nodes
    {
        'data': 0,
        'left':
        {
            'data': 1,
        },
    },
    {
        'data': 0,
        'right':
        {
            'data': 1,
        },
    },
    # more nodes
    {
        'data': 0,
        'left':
        {
            'data': 1,
            'left':
            {
                'data': 3
            },
            'right':
            {
                'data': 4
            }
        },
        'right':
        {
            'data': 2,
            'right': 
            {
                'data': 5
            }
        }
    },
    {
        'data': 0,
        'right':
        {
            'data': 1,
            'right':
            {
                'data': 2,
                'right':
                {
                    'data': 3
                }
            }
        }
    }
]


def get_tree(dct):
    if dct:
        data = dct["data"]
        left = get_tree(dct["left"]) if "left" in dct else None
        right = get_tree(dct["right"]) if "right" in dct else None
        return Node(data, left, right)
    return None


def get_trees():
    return [get_tree(dct) for dct in _trees]


def print_tree(root, val="data", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """
        Returns list of strings, width, height,
        and horizontal coordinate of the root.
        """
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


if __name__ == "__main__":
    for tree in get_trees():
        print_tree(tree)
        print()

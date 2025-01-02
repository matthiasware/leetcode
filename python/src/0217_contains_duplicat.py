"""
    217. Contains Duplicate
    Given an integer array nums, return true
    if any value appears at least twice in the array,
    and return false if every element is distinct.
"""

tests = [
    ([0], False),
    ([-1, 10], False),
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 0], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
]


def contains_duplicate_hashing(lst: list[int]) -> bool:
    """
    Time: O(n)
    Memo: O(n)
    """
    n = len(lst)
    return n != len(set(lst))


def contains_duplicate_naive(lst: list[int]) -> bool:
    """
    Time: O(n^2)
    Memo: O(1)
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False


def contains_duplicate_sort(lst: list[int]) -> bool:
    """
    Time: O(n log(n))
    Memo: O(1)
    """
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return True
    return False


if __name__ == "__main__":
    for lst, exp in tests:
        act = contains_duplicate_sort(lst)
        assert act == exp

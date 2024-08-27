"""
219. Contains Duplicate II

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Constraints:
-) 1 <= nums.length <= 10^5
-) -109 <= nums[i] <= 10^9
-) 0 <= k <= 10^5
"""

from collections import namedtuple, defaultdict

Test = namedtuple("Test", ("lst", "k", "exp"))

tests = (
    Test([1, 0, 1, 1], 1, True),
    Test([1, 2, 3, 1], 3, True),
    Test([1, 2, 3, 1, 2, 3], 2, False),
    Test([1], 1, False),
    Test([1, 2], 1, False),
    Test([1, 1], 1, True),
    Test([1, 1], 10, True),
)


def contains_duplicates_window(lst: list[int], k: int) -> bool:
    """
        Time: O(n*k)
        Memo: O(1)
    """
    for i in range(len(lst) - 1):
        for j in range(i+1, min(i+k+1, len(lst))):
            if lst[i] == lst[j]:
                return True
    return False


def contains_duplicates_window_count(lst: list[int], k: int) -> bool:
    """
        Idea: static sliding window with count set.
              for each slide, check if new entry is already in window.
        Time: O(n)
        Memo: O(k)
    """
    nums = set()
    for idx in range(len(lst)):
        if idx > k:
            nums.remove(lst[idx - k - 1])
        num = lst[idx]
        if num in nums:
            return True
        nums.add(num)
    return False


if __name__ == "__main__":
    for lst, k, exp in tests:
        act = contains_duplicates_window_count(lst, k)
        assert act == exp, f"exp='{exp}', act='{act}"

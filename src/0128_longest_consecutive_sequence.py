"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Constraints:
-) 0 <= nums.length <= 10^5
-) -10^9 <= nums[i] <= 10^9
"""

tests = [
    ([100, 4, 200, 1, 3, 2], 4),  # 1, 2, 3, 4
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
]


def longest_conecutive_by_sort(nums: list[int]) -> int:
    """
    Time: O(n*log(n))
    Memo: O(1)
    """
    nums.sort()
    len_max = 0
    len_cur = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            len_cur += 1
            len_max = max(len_max, len_cur)
        else:
            len_cur = 1
    return len_max


def longest_consecutive(nums: list[int]) -> int:
    """
    Time: O(n)
    Memo: O(n)

    1. Check if number can be start of a ss
    2. If so, culculate the length of the ss
    """
    s = set(nums)
    len_max = 0

    for n in nums:
        if n - 1 in s:
            continue

        len_cur = 1
        ele_cur = n + 1

        while ele_cur in s:
            len_cur += 1
            ele_cur += 1
        len_max = max(len_max, len_cur)
    return len_max


def longest_consecutive_simplified(nums: list[int]) -> int:
    """
    Same as above but simplified
    """
    s = set(nums)
    length_max = 0

    for n in nums:
        if n - 1 not in s:
            length = 1
            while n + length in s:
                length += 1
            length_max = max(length_max, length)
    return length_max


if __name__ == "__main__":
    for nums, exp in tests:
        act = longest_consecutive_simplified(nums)
        assert act == exp

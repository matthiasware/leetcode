"""
1. Two Sums

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Constraints:
-) 2 <= nums.length <= 10^4
-) 10^9 <= nums[i] <= 10^9
-) 10^9 <= target <= 10^9
"""

tests = [
    ([0, -1, 2, -3, 1], -2, [3, 4]),
    ([1, -2, 1, 0, 5], 0, []),
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    # map: num -> idx
    dct = {}
    for idx, n in enumerate(nums):
        if target - n in dct:
            return [dct[target - n], idx]
        dct[n] = idx
    return []


if __name__ == "__main__":
    for nums, target, exp in tests:
        act = two_sum(nums, target)
        assert act == exp

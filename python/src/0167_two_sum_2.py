"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers
that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.

Constraints:
    -) 2 <= numbers.length <= 3 * 10^4
    -) -1000 <= numbers[i] <= 1000
    -) numbers is sorted in non-decreasing order.
    -) -1000 <= target <= 1000
    -) The tests are generated such that there is exactly one solution.
"""

import bisect

tests = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
]


def two_sums_binsearch(nums, k):
    """
    Idea: iterate through array and do binary search for missing number
    Time: O(n*log(n))
    Memo: O(1)
    """
    for idx, n in enumerate(nums):
        target = k - n
        idx_target = bisect.bisect_left(nums, target, lo=idx + 1)
        if nums[idx_target] == target:
            return [idx + 1, idx_target + 1]
    return []


def two_sums(nums, k):
    """
    Time: O(n)
    Memo: O(1)
    """
    i = 0
    j = len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s < k:
            i += 1
        elif s > k:
            j -= 1
        else:
            return [i + 1, j + 1]
    return []


if __name__ == "__main__":
    for nums, target, exp in tests:
        act = two_sums(nums, target)
        assert act == exp

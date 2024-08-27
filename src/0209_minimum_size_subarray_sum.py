"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return
the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length.

Example 2: target = 4, nums = [1,4,4]
Output: 1
Example 3: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4

Follow up:
If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log(n)).
"""

from collections import namedtuple
import math

Test = namedtuple("Test", ("nums", "target", "exp"))

tests = (
    Test([2, 3, 1, 2, 4, 3], 7, 2),
    Test([1, 4, 4], 4, 1),
    Test([1, 1, 1, 1, 1, 1, 1, 1], 11, 0),
)


def min_subarray_len(nums: list[int], target: int) -> int:
    """
        Idea: dynamic sliding window and track minlen and current sum.
        Time: O(n)
        Memo: O(1)
    """
    minlen = len(nums) + 1
    csum = 0
    j = 0
    for i in range(len(nums)):
        csum += nums[i]
        while csum >= target:
            minlen = min(minlen, i - j + 1)
            csum -= nums[j]
            j += 1
    if minlen > len(nums):
        minlen = 0
    return minlen


if __name__ == "__main__":
    for nums, target, exp in tests:
        act = min_subarray_len(nums, target)
        print(act, exp)

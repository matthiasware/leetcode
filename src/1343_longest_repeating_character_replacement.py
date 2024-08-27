"""
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Given an array of integers arr and two integers k and threshold,
return the number of sub-arrays of size k and average greater than or equal to threshold.

Example 1:
arr = [2,2,2,2,5,5,5,8], k = 3, th = 4 out: 3
Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6.
All other sub-arrays of size 3 have averages less than 4 (the threshold).

Example 2:
arr = [11,13,17,23,29,31,7,5,2,3], k = 3, th = 5 out: 6
The first 6 sub-arrays of size 3 have averages greater than 5.
Note that averages are not integers.

Constraints:
-) 1 <= arr.length <= 10^5
-) 1 <= arr[i] <= 10^4
-) 1 <= k <= arr.length
-) 0 <= threshold <= 10^4
"""

from collections import namedtuple

Test = namedtuple("Test", ("nums", "k", "th", "exp"))
tests = (
    Test([2, 2, 2, 2, 5, 5, 5, 8], 3, 4, 3),
    Test([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5, 6),
)


def num_of_subarrays(nums: list[int], k: int, th: int) -> int:
    """
        Idea: Sliding window of size k
              Track sum and counts
        Time: O(n)
        Memo: O(1)
    """
    csum = 0
    counts = 0
    for idx in range(len(nums)):
        csum += nums[idx]
        if idx >= k:
            csum -= nums[idx - k]
        if idx >= (k-1) and csum / k >= th:
            counts += 1
    return counts


if __name__ == "__main__":
    for nums, k, th, exp in tests:
        act = num_of_subarrays(nums, k, th)
        print(exp, act)

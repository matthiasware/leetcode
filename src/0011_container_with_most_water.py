"""
11. Container With Most Water
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
-) n == height.length
-) 2 <= n <= 10^5
-) 0 <= height[i] <= 10^4
"""

tests = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 8, 14, 2, 5, 4, 13, 3, 7], 52),
    ([1, 10, 6, 2, 5, 4, 10, 3, 7], 50),
    ([1, 1], 1),
]


def max_area_naive(height):
    """
    Time: O(n^2)
    Memo: O(1)
    """
    amax = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            amax = max(amax, area)
    return amax


def max_area(height):
    """
    Time: O(n)
    Memo: O(1)
    Intuition: for a border it only makes sense to search for a new one,
               if it limits the water that the bucket can hold.
               Therefore search always from the lower border.
    """
    area_max = 0
    l = 0
    r = len(height) - 1
    while l < r:
        left, right = height[l], height[r]

        area_cur = min(left, right) * (r - l)
        area_max = max(area_max, area_cur)

        if left < right:
            l += 1
        else:
            r -= 1
    return area_max


if __name__ == "__main__":
    for nums, exp in tests:
        act = max_area_naive(nums)
        print(act, exp)
        assert act == exp

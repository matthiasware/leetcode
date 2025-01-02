"""
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1: heights = [2,1,5,6,2,3] Output: 10
    0 2 |**
    1 1 |*
    2 5 |*****
    3 6 |******
    4 2 |**
    5 3 |***
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2: heights = [2,4] Output: 4

Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""

from collections import namedtuple

Test = namedtuple("Test", ["heights", "exp"])
tests = [
    Test([1], 1),
    Test([1, 2, 3], 4),
    Test([2, 1, 5, 6, 2, 3], 10),
    Test([2, 4], 4),
    Test([7, 1, 7, 2, 2, 4], 8)
]


def largest_area(heights: list[int]) -> int:
    """
    Time: O(n)
    Memo: O(n)
    Idea:
        - store heights on stack with index
        - only store increasing heights on stack
        - iterate through list
        - for an element:
            - if bigger add to stack
            - if smaller, pop from stack and calculate area
    """
    stack = []  # (index, height)
    max_area = 0
    for i, hi in enumerate(heights):
        start = i  # the starting index for area of height hi
        while stack and hi < stack[-1][1]:
            j, hj = stack.pop()
            area = hj * (i - j)
            max_area = max(max_area, area)
            start = j
        stack.append((start, hi))

    # calculate area for remeaining elements
    for i, height in stack:
        max_area = max(max_area, (len(heights) - i) * height)
    return max_area


if __name__ == "__main__":
    for heights, exp in tests:
        act = largest_area(heights)
        assert act == exp

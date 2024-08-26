"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map
where the width of each bar is 1,
compute how much water it can trap after raining.

Constraints:

-) n == height.length
-) 1 <= n <= 2 * 10^4
-) 0 <= height[i] <= 10^5
"""

tests = [
    ([1], 0),
    ([1, 0], 0),
    ([4, 0, 1, 2], 3),
    ([1, 0, 1], 1),
    ([2, 0, 3], 2),
    ([1, 2, 1, 0, 1, 2], 4),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    # ([4, 2, 0, 3, 2, 5], 9),
]


def trap_first(height):
    """
    Idea: Extra Memory to store for every element the max left and right hight.
    Time: O(n)
    Memo: O(n)
    """
    if len(height) < 3:
        return 0
    height_max = 0
    height_left = [0] * len(height)
    for i in range(1, len(height) - 1):
        height_max = max(height_max, height[i - 1])
        height_left[i] = height_max

    height_max = 0
    height_right = [0] * len(height)
    for i in reversed(range(1, len(height) - 1)):
        height_max = max(height_max, height[i + 1])
        height_right[i] = height_max

    volume = 0
    for i in range(1, len(height) - 1):
        volume += max(0, min(height_left[i], height_right[i]) - height[i])
    return volume


def trap(height):
    """
    Time: O(n)
    Memo: O(1)
    Ideas:
        - Pointers left and right
        - Safe max_left and max_right
        - Can only trap water if height smaller than barrier

    """
    if len(height) < 3:
        return 0

    left_max = height[0]
    right_max = height[-1]
    volume = 0

    i_left = 0
    i_right = len(height) - 1

    while i_left < i_right:
        if left_max < right_max:
            i_left += 1
            left_max = max(left_max, height[i_left])
            volume += left_max - height[i_left]
        else:
            i_right -= 1
            right_max = max(right_max, height[i_right])
            volume += right_max - height[i_right]
    return volume


if __name__ == "__main__":
    for height, exp in tests:
        act = trap(height)
        assert act == exp

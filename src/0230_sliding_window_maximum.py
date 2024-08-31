"""
239. Sliding Window Maximum

You are given an array of integers nums,
there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

from collections import namedtuple, deque

Test = namedtuple("Test", ("nums", "k", "exp"))

tests = [
    Test([1], 1, [1]),
    Test([1, 3, 0, 2, 1], 3, [3, 3, 2]),
    Test([1, 2, 1, 0, 4, 2, 6], 3, [2, 2, 4, 4, 6]),
    Test([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
]


def max_sliding_window_naive(nums: list[int], k: int) -> list[int]:
    """
    Time: O(n*k)
    Memo: O(k)
    """
    maxima = []
    for idx in range(len(nums) - k + 1):
        maxima.append(max(nums[idx: idx + k]))
    return maxima


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """
    Idea: 
        - represent window via deque
        - store indices instead of elements
        - first item in deque always reperesents the current maximum
        - if we add an item, remove all other items that are smaller
        - remove first: O(1)
        - insert last: O(1)
    Time: O(n)
    Memo: O(k)
    """
    maxima = []
    # store indices and only elements that could be maxima
    window = deque()
    for idx, n in enumerate(nums):

        # remove all nums in window that are smaller than n
        while window and n > nums[window[-1]]:
            window.pop()

        # add element to window
        window.append(idx)

        # contract window to correct length
        if window[0] < (idx - k + 1):
            window.popleft()

        if idx >= k - 1:
            maxima.append(nums[window[0]])
    return maxima


if __name__ == "__main__":
    for nums, k, exp in tests:
        act = max_sliding_window(nums, k)
        assert act == exp

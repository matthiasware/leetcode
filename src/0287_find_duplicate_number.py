"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using O(1) extra space!

Example 1: nums = [1,3,4,2,2] Output: 2
Example 2: nums = [3,1,3,4,2] Output: 3
Example 3: nums = [3,3,3,3,3] Output: 3

Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n

All the integers in nums appear only once
except for precisely one integer which appears two or more times.

Follow up:
- How can we prove that at least one duplicate number must exist in nums?
    -> max != n for array of length n
- Can you solve the problem in linear runtime complexity?
    -> using sets to store seen numbers
- Can you solve the problem without modifying the array nums and using O(1) extra space?
"""

tests = [([1, 3, 4, 2, 2], 2),
         ([3, 1, 3, 4, 2], 3),
         ([3, 3, 3, 3, 3], 3)]


def find_duplicate_naive(nums: list[int]) -> int:
    """
    Time: O(n^2)
    Memo: O(1)
    """
    for n in range(1, len(nums)):
        visited = False
        for num in nums:
            if n == num:
                if visited:
                    return num
                visited = True


def find_duplicate_set(nums: list[int]) -> int:
    """
        Time: O(n)
        Memo: O(n)
    """
    visited = set()
    for n in nums:
        if n in visited:
            return n
        visited.add(n)


def find_duplicate(nums: list[int]) -> int:
    """
       Time: O(n) better than quadratic
       Memo: O(1)
       Idea:
        - Using Floyd's algorithm! Really hard
        - Linked List problem cycle problem
        - Assume the list is a linked list and use cycle detection
    """
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # i have no idea why this works
    slow2 = 0
    while True:
        slow2 = nums[slow2]
        slow = nums[slow]
        if slow2 == slow:
            return slow


if __name__ == "__main__":
    for nums, exp in tests:
        act = find_duplicate(nums)
        print(exp, act, nums)

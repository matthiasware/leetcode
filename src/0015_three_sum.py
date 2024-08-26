"""
3 Sum

Given an integer array nums,
return all the triplets
    nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
    -) 3 <= nums.length <= 3000
    -) -10^5 <= nums[i] <= 10^5
"""

tests = (
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
)


def three_sums(nums):
    """
    Idea: So hard ...
    Time: O(n log n) + O(n^2) -> O(n^2)
    Memo: O(1)
    """
    res = []
    nums.sort()
    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            # required to eliminate duplicates [-1,-1,0,1]
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            total = n + nums[l] + nums[r]
            if total == 0:
                res.append([n, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    # required to eliminate duplicates
                    # [-2, 0, 0, 2, 2]
                    l += 1
            elif total < 0:
                l += 1
            else:
                r -= 1
    return res


if __name__ == "__main__":
    for nums, exp in tests:
        act = three_sums(nums)
        assert act == exp, f"act={act} != exp={exp}"

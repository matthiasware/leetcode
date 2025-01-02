"""
238. Product of Array Except Self

Given an integer array nums,
return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time
and without using the division operation.
"""


tests = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
]


def product_of_array_smart(nums: list[int]) -> list[int]:
    # if one zero -> everything 0 except idx(0)
    # if > 1 zeros -> everything 0
    # otherwise prod
    prod = 1
    n_zeros = 0
    for n in nums:
        if n == 0:
            n_zeros += 1
        else:
            prod *= n
    if n_zeros == 0:
        res = [prod // n for n in nums]
    elif n_zeros == 1:
        res = [0 if n != 0 else prod for n in nums]
    else:
        res = [0] * len(nums)
    return res


def product_of_array_prefix_suffix(nums: list[int]) -> list[int]:
    """
    Time: O(n)
    Memo: O(n)
    prefix  1,1,2,0   1,1,2,6
    nums    1,2,0,3   1,2,3,2
    suffix  0,0,3,1  12,6,2,1
    """
    prefix = [1]
    prod = 1
    for n in nums[:-1]:
        prod *= n
        prefix.append(prod)

    suffix = [1]
    prod = 1
    for n in reversed(nums[1:]):
        prod *= n
        suffix.append(prod)
    suffix.reverse()

    res = []
    for i in range(len(nums)):
        res.append(prefix[i] * suffix[i])
    return res


if __name__ == "__main__":
    for nums, exp in tests:
        act = product_of_array_prefix_suffix(nums)
        assert act == exp
